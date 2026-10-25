# Templates

## Rôle

Ce dossier contient le gabarit HTML de l'interface de la calculatrice. Il fait partie du frontend de l'application. Ce dossier `templates/` est le dossier où Flask cherche les gabarits par défaut.

## Fichiers

- `index.html` : page de la calculatrice, avec l'écran de saisie, l'interface de boutons et les fonctions JavaScript qui remplissent ou effacent cet écran de saisie.

## Dépendances et hypothèses

- La page est rendue par Flask à partir de la fonction `index()` de `backend/app.py`. Cette fonction fournit la variable `result` à la page.
- La feuille de style est chargée depuis `static/style.css` avec `url_for`.
- Le champ de l'écran doit s'appeler `display`, car c'est le nom lu par `backend/app.py`. Le renommer empêche le calcul de fonctionner, à moins de le renommer également dans `backend/app.py`.
- Ce champ est en lecture seule, donc il ne peut être modifié que par les boutons de l'interface. Seul le bouton `=` envoie le formulaire au serveur.