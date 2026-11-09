# Italiano

This branch defaults to `it`. Pass `--lang` to override it. Read the [shared workflow](multilingual/README.md) before revising documentation.

## Italiano: review guidance

- Mantenere il registro e la forma delle istruzioni: tu, Lei, infinito o forma impersonale.
- Controllare accordi, articoli, preposizioni articolate e riferimenti dei pronomi; non imporre soggetti espliciti.
- Ridurre nominalizzazioni, forme burocratiche e calchi inglesi conservando i termini tecnici necessari.
- Distinguere può, deve, si consiglia e le negazioni. Non trasformare una possibilità in una garanzia.
- Conservare accenti, apostrofi, convenzioni decimali e uso locale delle unità; non tradurre codice o identificatori.
- Controllare che il gerundio abbia un soggetto coerente e non renda ambigua la sequenza delle operazioni.
- Eliminare premesse vuote e promesse non dimostrate. Ripetere un termine tecnico quando serve alla precisione.

## Commands

```bash
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --prompt
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py document.md
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --orig document.md document.taste.md --json
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

## Review example

È importante sottolineare che il solutore registra 20 campioni.

## Clear example

Il solutore registra 20 campioni.

These are contextual editing examples, not automatic substitutions. Preserve meaning, protected content and facts. Manual review remains required even when checks pass.
