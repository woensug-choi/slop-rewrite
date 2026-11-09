# Multilingual documentation review

This fork adds review profiles for English (`en`), Korean (`ko`), Japanese (`ja`),
Chinese (`zh`), German (`de`), French (`fr`), Spanish (`es`) and Italian (`it`).
They cover technical documentation rather than general-purpose translation.
The upstream Korean guides and commands remain available without changes to
their behavior. Do not run Korean sentence or morphology rules on other languages.

The code reports editorial patterns and prepares instructions for a writing
agent. It does not identify AI authorship, automatically rewrite files, call a
model, send documents over the network, or certify prose quality.

## Review and revise

Use Python 3.10 or later from the repository root. The multilingual tool needs
only the standard library.

```bash
# Read the language-specific instructions before editing.
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --lang ja --prompt

# Inspect an existing document. Style findings are advisory by default.
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --lang ja document.ja.md

# After a requested rewrite, compare against the untouched original.
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --lang ja --orig document.ja.md document.ja.taste.md --json

# Offline regression tests for all eight profiles.
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

`--lang` is explicit on the integration branch. Each `language/<code>` branch
also has a `.slop-language.json` default and a native-language `LANGUAGE.md`.
An explicit `--lang` always wins. Branches share the same implementation and
all eight profiles so fixes do not diverge. Update the shared implementation
first, then bring that commit to each language branch while preserving its
default. Do not merge a language branch's default into another language.

The profile is selected by content locale, not the language of a request to
the assistant. Regional tags such as `en-GB`, `fr-CA`, `zh-Hans` and `zh-Hant`
select the base-language profile. They do not convert spelling, locale,
punctuation, simplified/traditional characters, or measurements. Unsupported
languages fail with an error rather than falling back to Korean or English.

1. Identify the audience, document locale, existing register and source of truth.
2. Read `--prompt` and the source. Use style findings as questions, not replacement instructions.
3. Revise only where the text is unclear, repetitive or unsupported. Leave clear text alone.
4. Save a separate `.taste` file and notes. If repository editing is explicitly
   requested, preserve the original in Git and edit on a review branch instead.
5. Run `--orig`, inspect the complete diff, then run the repository's document
   build, link checks and tests. Compare claims against the source locale too.
6. Record meaningful changes, intentional invariant changes and unresolved
   questions. Do not publish or merge without the user's authorization.

## What each profile reviews

- **English:** direct subjects and verbs, countability and agreement, modality,
  existing US/UK spelling, unnecessary nominalization and unsupported promotion.
- **Korean:** particles and predicate agreement, spacing, consistent endings,
  translated constructions, technical noun lists and scope of negation.
- **Japanese:** particles, omitted subjects, modifier scope, consistent politeness,
  redundant honorifics and Japanese punctuation without code normalization.
- **Chinese:** topic continuity, classifiers, modifier order, concise verbs,
  simplified/traditional preservation and sentence boundaries without space-based word counts.
- **German:** case and gender agreement, compounds, verb position, nominal chains,
  address forms and DACH spelling conventions.
- **French:** agreement and pronouns, accents, apostrophes, non-breaking spaces,
  register and unnecessary nominalization without changing technical terminology.
- **Spanish:** regional address forms, agreement, accented characters, opening
  punctuation and gerunds that obscure the order of operations.
- **Italian:** agreement, contracted prepositions, subject consistency in gerunds,
  accents, register and bureaucratic phrasing.

## Safety and limits

The tool accepts Markdown, MDX and plain text. It masks code fences, inline and
indented code, front matter, Markdown tables, block quotations, explicit quotes,
HTML tags, comments, math, citations, placeholders and link destinations before
style checks. It uses NFC only for matching, never writes normalized text, and
does not use NFKC or whitespace-based CJK word limits.

`--orig` compares multisets of protected spans and exact numeric/unit spellings.
Both additions and removals are errors. This conservative check can flag an
intentional change, including quote punctuation or numeric formatting. Review
that change against the source rather than silently suppressing the result.
Repeated spans cannot disappear unnoticed, but rearranging identical protected
content is allowed. Numeric values and units embedded inside protected regions
are checked through the complete protected content.

This is not a full Markdown/MDX parser. Complex JSX, custom directives, escaped
markup and templates need their project's parser and human review. The checker
cannot prove that names, claims, negation, conditions, factual relationships,
translations or implicit heading anchors retain their meaning. Check these
manually and run link/build checks, even when the tool returns PASS.

Exit codes: `0` means no blocking findings; `1` means changed protected content
or numbers, or style findings with the opt-in `--fail-on-warnings`; `2` means
invalid input or an unavailable profile. JSON output always includes
`manual_review_required: true`. No result means the text is “human-written.”

## Tests and maintenance

Every profile contains native-language review/clear examples. Tests cover all
eight locales, cross-language rule isolation, decomposed accents and Hangul,
traditional Chinese, source line numbers, protected Markdown, numbers and
units, non-mutating CLI behavior and exit codes. The multilingual suite is
also included in the upstream `run_ci.py` aggregate check.

Keep profiles small and reviewable. Add native-language positive and negative
examples with each rule change. Treat a phrase as a review cue, never as proof
of poor writing, and preserve valid technical meanings when deciding to keep it.
