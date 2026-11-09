# Español

This branch defaults to `es`. Pass `--lang` to override it. Read the [shared workflow](multilingual/README.md) before revising documentation.

## Español: review guidance

- Mantener la variedad regional y el tratamiento elegido: tú, usted, vosotros o redacción impersonal.
- Revisar la concordancia de género y número y los referentes de pronombres, sin forzar sujetos explícitos.
- Evitar calcos del inglés y nominalizaciones innecesarias. Conservar la terminología técnica establecida.
- Distinguir puede, debe, se recomienda y las negaciones; mantener el alcance de condiciones y excepciones.
- Revisar usos del gerundio que expresen una consecuencia posterior y puedan ocultar el orden de los pasos.
- Conservar tildes, signos de apertura y convenciones decimales; no modificar comandos, rutas ni identificadores.
- Reducir frases vacías y valoraciones sin respaldo. No sustituir términos precisos solo para evitar repeticiones.

## Commands

```bash
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --prompt
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py document.md
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --orig document.md document.taste.md --json
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

## Review example

Cabe destacar que el solucionador registra 20 muestras.

## Clear example

El solucionador registra 20 muestras.

These are contextual editing examples, not automatic substitutions. Preserve meaning, protected content and facts. Manual review remains required even when checks pass.
