# 日本語

This branch defaults to `ja`. Pass `--lang` to override it. Read the [shared workflow](multilingual/README.md) before revising documentation.

## 日本語: review guidance

- 敬体（です・ます）と常体（だ・である）は文書の既存方針に合わせ、混在を避ける。
- 助詞の対応、修飾節の係り先、主語の省略が誤読を招かないか確認する。
- 不要な名詞化や重複する敬語を減らす。必要な受け身と技術用語は残す。
- 可能・義務・推奨・予定・否定を区別する。「できます」を必ず実行する意味に変えない。
- 和文の句読点と括弧を既存の表記に合わせる。半角・全角の変換をコードや数値へ一括適用しない。
- カタカナ語と略語の表記を揃える。説明のない新しい訳語を作らない。
- 空白区切りの語数を基準に文を分割しない。手順と条件の関係が読める長さに整える。

## Commands

```bash
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --prompt
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py document.md
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --orig document.md document.taste.md --json
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

## Review example

特筆すべきことに、ソルバーは20個のサンプルを記録します。

## Clear example

ソルバーは20個のサンプルを記録します。

These are contextual editing examples, not automatic substitutions. Preserve meaning, protected content and facts. Manual review remains required even when checks pass.
