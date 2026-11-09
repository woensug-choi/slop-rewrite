# English

This branch defaults to `en`. Pass `--lang` to override it. Read the [shared workflow](multilingual/README.md) before revising documentation.

## English: review guidance

- Keep the existing US/UK spelling and the document’s chosen voice; do not switch dialects.
- Use a concrete subject and verb when the actor is known. Keep passive voice when the actor is unknown or irrelevant.
- Remove empty lead-ins and unsupported superlatives; retain technical terms with precise meanings.
- Keep may, can, must, should and negation distinct. A possibility is not a guarantee or requirement.
- Keep articles, countability, singular/plural agreement and parallel imperative steps natural.
- Preserve API names, units, decimal points and citations; use sentence case only when it fits the existing heading convention.

## Commands

```bash
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --prompt
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py document.md
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --orig document.md document.taste.md --json
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

## Review example

It should be noted that the solver records 20 samples.

## Clear example

The solver records 20 samples.

These are contextual editing examples, not automatic substitutions. Preserve meaning, protected content and facts. Manual review remains required even when checks pass.
