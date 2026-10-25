# Calculatrice Flask

LOG3000 - TP3

Numéro d'équipe : 25

## Description

### But

Ce projet est une calculatrice web simple construite avec la bibliothèque Flask de Python. L'interface (en HTML/CSS) permet d'entrer une opération entre deux nombres (addition, soustraction, multiplication ou division) à l'aide des boutons affichés à l'écran.
Le serveur Python effectue le calcul puis renvoie le résultat à la page.

Ce dépôt a pour but d'encadrer la gestion des versions et des changements du projet afin de faciliter la collaboration au sein de l'équipe lors de l'évolution du code et de l'ajout de fonctionnalités. La base de code de la calculatrice y est reprise, documentée et testée. Les bogues sont corrigés en suivant un flux de contribution basé sur les issues, les branches et les pull requests.

### Portée

La calculatrice prend en charge :

- les opérations de base : `+`, `-`, `*` et `/`
- une seule opération à la fois entre 2 nombres entiers
- un résultat décimal lorsque c'est nécessaire
- un message d'erreur si l'expression est invalide ou dans le cas d'une division par zéro

La calculatrice ne permet pas :

- les nombres décimaux ou négatifs en entrée
- les calculs à plusieurs opérateurs ou avec parenthèses
- la saisie au clavier car il faut utiliser les boutons d'interface

## Prérequis

- [Git](https://git-scm.com/install/)
- [Python](https://www.python.org/downloads/) 3.9 ou plus récent (3.11+ recommandé)
- pip (installé avec Python)

## Installation

1. Cloner le dépôt :

    ```shell
    git clone https://github.com/jadchahbour/log3000-tp3-calculatrice.git
    cd log3000-tp3-calculatrice
    ```

2. Créer et activer un environnement virtuel (optionnel, mais recommandé) :

    macOS / Linux :

    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```

    Windows (PowerShell) :

    ```powershell
    python -m venv venv
    venv\Scripts\Activate.ps1
    ```

3. Installer Flask :

    ```shell
    pip install flask
    ```

## Utilisation

1. Lancer le serveur depuis la racine du projet :

    macOS / Linux :

    ```shell
    python3 backend/app.py
    ```

    Windows (PowerShell) :

    ```powershell
    python backend/app.py
    ```

2. Ouvrir [http://127.0.0.1:5000](http://127.0.0.1:5000) dans un navigateur.

3. Entrer un calcul avec les boutons, par exemple appuyer sur `9`, `/`, `2`.

4. Appuyer sur `=`. Le résultat du calcul va s'afficher à l'écran (ici, `4.5`). Si le calcul est invalide (aucun ou plusieurs opérateurs, opérateur au début ou à la fin, division par zéro), un message d'erreur commençant par `Error:` s'affiche à la place du résultat.

5. Appuyer sur `C` pour effacer la saisie.

## Tests

## Contribution

### Issues

Un changement commence par une issue dans GitHub qui décrit la tâche ou le problème. Chaque issue est assignée à un membre de l'équipe ainsi qu'à un label.

Voici les labels utilisés :

- `bug` : comportement incorrect de l'application
- `documentation` : ajout ou modification de documentation
- `test` : ajout ou modification de tests
- `enhancement` : nouvelle fonctionnalité ou amélioration

Pour un bogue, il faut inclure les étapes de reproduction ou les cas de test en échec.

### Branches

La branche `main` est protégée. Il n'est pas possible de la supprimer ou d'y faire directement des commits. Chaque issue est traitée dans sa propre branche, créée à partir de `main`. Une branche créée doit suivre ce format :

```
type/numéro-issue-description-courte
```

La description est écrite en français.

Types de branches :

- `feat` : pour les nouvelles fonctionnalités
- `fix` : pour les corrections de bogues
- `docs` : pour les mises à jour de documentation
- `test` : pour l'ajout ou modification de tests
- `refactor` : pour la refactorisation du code
- `chore` : pour la maintenance ou mise en place du projet 

Par exemple, `fix/5-division-par-zéro`.

### Commits

Les messages de commits suivent le format `type: description`. Les types sont les mêmes que pour les branches. Les commits peuvent se terminer par le numéro de l'issue concernée, le cas échéant. Ils sont écrits en français.

Par exemple, `fix: correction de la division par zéro (#5)`.

Les commits peuvent contenir un corps de message afin de donner plus de détails, le cas échéant.

### Pull requests

Lorsque le travail sur une branche est terminé, il faut :

1. Lancer les tests en local et vérifier qu'ils passent tous.
2. Pousser la branche sur Github et ouvrir une PR vers `main`.
3. Indiquer dans la description ce qui a été effectué, le résultat des tests, puis ajouter `Closes #numéro-issue` pour que l'issue associée ferme automatiquement lors de la fusion.
4. Passer en revue la pull request puis la fusionner dans `main`. Aucune approbation n'est nécessaire car l'équipe ne contient qu'un membre!
5. Supprimer la branche source une fois la fusion effectuée.