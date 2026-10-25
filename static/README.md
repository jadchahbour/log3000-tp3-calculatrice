# Static

## Rôle

Ce dossier contient tous les fichiers statiques de l'interface. Ces fichers statiques sont servis tels quels par Flask. Ce dossier fait partie du frontend de l'application.

## Fichiers

- `style.css` : mise en forme de la calculatrice (page centrée, couleurs de la calculatrice, et styles des boutons).

## Dépendances et hypothèses

- Flask sert ce dossier à l'adresse `/static/`, par exemple `http://127.0.0.1:5000/static/style.css`. Son emplacement est indiqué à la création de l'application dans `backend/app.py`.
- Le style repose sur les classes et identifiants utilisés dans `templates/index.html` : `.calculator`, `.buttons`, `.btn`, `.operator` et `#display`. Si l'un d'eux est renommé dans le HTML, il faut aussi le modifier dans le fichier `style.css`.
- Aucune bibliothèque externe n'est utilisée.