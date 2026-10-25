# backend

## Rôle

Ce dossier contient la logique côté serveur de la calculatrice. Il reçoit l'expression envoyée par l'interface, l'analyse, effectue le calcul et renvoie la page avec le résultat.

## Fichiers

- `app.py` : crée l'application Flask et définit la route `/`. Ce fichier contient aussi la fonction `calculate()`, qui découpe l'expression et appelle l'opération correspondante.
- `operators.py` : fonctions de calcul `add()`, `subtract()`, `multiply()` et `divide()`.

## Dépendances et hypothèses

- Flask doit être installé avec `pip install flask`.
- Les dossiers `templates/` et `static/` se trouvent à la racine du projet. Leurs chemins sont indiqués à la création de l'application dans `app.py`.
- `app.py` importe `operators.py`.
- L'application doit donc être lancée avec `python3 backend/app.py` depuis la racine du projet.
- L'expression reçue contient une seule opération entre deux nombres. Les nombres négatifs ne sont pas pris en charge.
- `operators.py` ne fait aucune validation. La validation est effectuée par la fonction `calculate()` dans `app.py` qui vérifie l'expression avant d'appeler les fonctions de calcul.
- Toutes les erreurs sont attrapées dans `index()` et affichées à l'écran avec le préfixe `Error:`.