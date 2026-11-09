# Français

This branch defaults to `fr`. Pass `--lang` to override it. Read the [shared workflow](multilingual/README.md) before revising documentation.

## Français: review guidance

- Conserver le registre et le choix entre vous, infinitif et formulation impersonnelle dans les procédures.
- Vérifier les accords de genre et de nombre, les participes et le référent des pronoms.
- Réduire les nominalisations et les calques de l’anglais sans remplacer les termes techniques établis.
- Distinguer possibilité, obligation, recommandation et négation. Ne pas transformer « peut » en garantie.
- Conserver la variante régionale, les accents, les apostrophes et la ponctuation française, notamment les espaces insécables existantes.
- Ne pas convertir les virgules décimales, unités, commandes ou identifiants API pendant une simple révision stylistique.
- Supprimer les amorces vides et les promesses sans preuve. Garder les limites et les sources de chaque affirmation.

## Commands

```bash
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --prompt
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py document.md
python -X utf8 .claude/skills/slop-rewrite/scripts/check_multilingual.py --orig document.md document.taste.md --json
python -X utf8 .claude/skills/slop-rewrite/tests/test_multilingual.py
```

## Review example

Il convient de noter que le solveur enregistre 20 échantillons.

## Clear example

Le solveur enregistre 20 échantillons.

These are contextual editing examples, not automatic substitutions. Preserve meaning, protected content and facts. Manual review remains required even when checks pass.
