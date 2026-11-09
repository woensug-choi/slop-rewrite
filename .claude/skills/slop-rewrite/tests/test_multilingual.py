"""Offline multilingual contract tests; run directly with Python 3."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import unicodedata

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_multilingual.py"
SPEC = importlib.util.spec_from_file_location("multilingual", SCRIPT)
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)


class Languages(unittest.TestCase):
    def test_exact_locale_set(self):
        self.assertEqual(set(tool.LANGUAGES), {"en", "ko", "ja", "zh", "de", "fr", "es", "it"})
        self.assertEqual({p.stem for p in tool.PROFILE_DIR.glob("*.json")}, set(tool.LANGUAGES))

    def test_all_profiles_and_native_examples(self):
        for language in tool.LANGUAGES:
            with self.subTest(language=language):
                profile = tool.load_profile(language)
                self.assertGreaterEqual(len(profile["guidance"]), 6)
                self.assertGreaterEqual(len(profile["rules"]), 4)
                self.assertTrue(tool.inspect_style(profile["examples"]["review"], profile))
                self.assertFalse(tool.inspect_style(profile["examples"]["clear"], profile))
                self.assertFalse(tool.compare(profile["examples"]["review"], profile["examples"]["clear"]))
                prompt = tool.build_prompt(profile)
                self.assertIn(profile["name"], prompt)
                self.assertIn(profile["guidance"][0], prompt)
                self.assertIn("negation", prompt)

    def test_no_cross_language_rule_leakage(self):
        for language in tool.LANGUAGES:
            profile = tool.load_profile(language)
            for other in tool.LANGUAGES:
                if other != language:
                    with self.subTest(language=language, other=other):
                        sample = tool.load_profile(other)["examples"]["review"]
                        self.assertEqual(tool.inspect_style(sample, profile), [])

    def test_every_rule_has_native_regression_example(self):
        for language in tool.LANGUAGES:
            profile = tool.load_profile(language)
            for rule in profile["rules"]:
                with self.subTest(rule=rule["id"]):
                    findings = tool.inspect_style(rule["example"], profile)
                    self.assertIn(rule["id"], [f["rule"] for f in findings])
                    self.assertFalse(tool.inspect_style(f"```text\n{rule['example']}\n```", profile))

    def test_nfc_accents_and_hangul(self):
        for language in ("ko", "fr", "it"):
            profile = tool.load_profile(language)
            sample = profile["examples"]["review"]
            self.assertEqual(tool.inspect_style(sample, profile), tool.inspect_style(unicodedata.normalize("NFD", sample), profile))

    def test_regional_aliases(self):
        for value, expected in [("en-GB", "en"), ("pt-BR", None), ("zh_Hant", "zh"), ("zh-CN", "zh"), ("fr-CA", "fr")]:
            if expected:
                self.assertEqual(tool.canonical_language(value), expected)
            else:
                with self.assertRaises(ValueError):
                    tool.canonical_language(value)

    def test_traditional_chinese_stays_traditional(self):
        text = "需要強調的是，求解器會記錄20個樣本。"
        self.assertTrue(tool.inspect_style(text, tool.load_profile("zh")))
        self.assertIn("简体或繁体", tool.build_prompt(tool.load_profile("zh")))

    def test_word_boundaries(self):
        self.assertFalse(tool.inspect_style("Prevolutionary is an identifier.", tool.load_profile("en")))


class ProtectedContent(unittest.TestCase):
    SAMPLE = "It should be noted that"

    def test_excluded_regions(self):
        sample = self.SAMPLE
        regions = [
            f"```python\n{sample}\n```", f"~~~~\n{sample}\n~~~~", f"`{sample}`", f"``{sample} ` x``",
            f"> {sample}", f"    {sample}", f"---\ntitle: {sample}\n---",
            f"<!-- {sample} -->", f'<div title="{sample}">', f"${sample}$", f"$$\n{sample}\n$$",
            f"| Header |\n| --- |\n| {sample} |", f"A | B\n--- | ---\n{sample} | X",
            f"[label](https://example.org/{sample.replace(' ', '%20')})", f'“{sample}”', f'«{sample}»',
            f"[ref]: {sample}", f"{{{{ {sample} }}}}",
        ]
        for region in regions:
            with self.subTest(region=region):
                self.assertFalse(tool.inspect_style(region, tool.load_profile("en")))
                self.assertTrue(tool.compare(region, region.replace(sample, "Changed")) or sample not in region)

    def test_unclosed_fences(self):
        self.assertEqual(tool.prose("~~~\n" + self.SAMPLE).strip(), "")

    def test_link_labels_are_reviewable_destinations_preserved(self):
        text = f"[{self.SAMPLE}](https://example.com/a_(b)#c)"
        self.assertTrue(tool.inspect_style(text, tool.load_profile("en")))
        self.assertFalse(tool.compare(text, text.replace(self.SAMPLE, "Details")))
        self.assertTrue(tool.compare(text, text.replace("a_(b)", "other")))

    def test_line_numbers(self):
        text = "```\nprotected\n```\n\n" + self.SAMPLE + " the output is saved."
        self.assertEqual(tool.inspect_style(text, tool.load_profile("en"))[0]["line"], 5)

    def test_document_move_does_not_change_protected_multiset(self):
        self.assertFalse(tool.compare("`a`\n\n`b`", "`b`\n\n`a`"))

    def test_repeated_code_cannot_silently_disappear(self):
        self.assertTrue(tool.compare("`a` and `a`", "`a`"))

    def test_numbers_units_dates_and_cjk(self):
        for before, after in [("20 ms", "20 s"), ("1,5 m", "1.5 m"), ("20个样本", "21个样本"),
                              ("값은20이다", "값은21이다"), ("20個", "21個"), ("−5 °C", "5 °C"),
                              ("1\u202f000 m", "100 m"), ("2026-11-09", "2026-11-10")]:
            with self.subTest(before=before):
                self.assertTrue(tool.compare(before, after))

    def test_newline_normalization_is_allowed(self):
        self.assertFalse(tool.compare("```\r\nx\r\n```\r\n", "```\nx\n```\n"))

    def test_apostrophe_is_not_quotation(self):
        self.assertIn("l’analyse", tool.prose("Vérifier l’analyse et l’API."))


class CLI(unittest.TestCase):
    def run_tool(self, *args):
        return subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), *map(str, args)], capture_output=True, text=True, encoding="utf-8")

    def test_prompt_json_and_unknown_locale(self):
        result = self.run_tool("--lang", "ja", "--prompt", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["language"], "ja")
        self.assertTrue(json.loads(result.stdout)["manual_review_required"])
        self.assertEqual(self.run_tool("--lang", "xx", "--prompt").returncode, 2)

    def test_readonly_warning_and_strict_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.md"
            path.write_text("It should be noted that the solver records 20 samples.", encoding="utf-8")
            before = path.read_bytes()
            self.assertEqual(self.run_tool("--lang", "en", path).returncode, 0)
            self.assertEqual(self.run_tool("--lang", "en", "--fail-on-warnings", path).returncode, 1)
            self.assertEqual(path.read_bytes(), before)

    def test_fidelity_and_invalid_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            old, new = Path(directory) / "old.md", Path(directory) / "new.md"
            old.write_text("20 ms", encoding="utf-8")
            new.write_text("21 ms", encoding="utf-8")
            self.assertEqual(self.run_tool("--lang", "en", "--orig", old, new).returncode, 1)
            self.assertEqual(self.run_tool("--lang", "en", "--orig", old, old, new).returncode, 2)
            self.assertEqual(self.run_tool("--lang", "en", Path(directory) / "missing.md").returncode, 2)
            self.assertEqual(self.run_tool("--lang", "en", Path(directory) / "x.html").returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
