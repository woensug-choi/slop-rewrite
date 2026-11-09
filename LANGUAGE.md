# Deutsch

This branch defaults to `de`. Pass `--lang` to override it. Read the [shared workflow](multilingual/README.md) before revising documentation.

## Deutsch: review guidance

- Die gewählte Anrede beibehalten: du, Sie oder unpersönliche Anleitung. Nicht ungefragt wechseln.
- Kasus, Artikel, Genus und Numerus prüfen. Zusammensetzungen und Großschreibung deutscher Substantive erhalten.
- Verbklammer und Stellung des finiten Verbs beachten. Lange Nominalketten auflösen, ohne fachliche Bezüge zu verändern.
- Passiv verwenden, wenn der Handelnde unbekannt oder unwichtig ist; keinen Akteur erfinden.
- Kann, muss, soll, darf und Negationen unterscheiden. Bedingungen und Gültigkeitsbereiche nicht verkürzen.
- Dezimalkomma, Maßeinheiten, ß/ss und gewählte DACH-Variante erhalten; Quellcode und Bezeichner nicht eindeutschen.
- Füllformeln und unbelegte Wertungen streichen. Fachbegriffe nicht allein zur Variation durch Synonyme ersetzen.

## Commands

```bash
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --prompt
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py document.md
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --orig document.md document.taste.md --json
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

## Review example

Es ist wichtig zu beachten, dass der Solver 20 Proben speichert.

## Clear example

Der Solver speichert 20 Proben.

These are contextual editing examples, not automatic substitutions. Preserve meaning, protected content and facts. Manual review remains required even when checks pass.
