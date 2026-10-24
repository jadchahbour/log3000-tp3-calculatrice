# Calculatrice Flask

LOG3000 - TP3

Numéro d'équipe : 25

## Objectif

Ce projet est une calculatrice web simple construite avec la bibliothèque Flask de Python. L'interface (en HTML/CSS) permet d'entrer une opération entre deux nombres (addition, soustraction, multiplication ou division) à l'aide des boutons affichés à l'écran.
Le serveur Python effectue le calcul puis renvoie le résultat à la page.

Ce dépôt a pour but d'encadrer la gestion des versions et des changements du projet afin de faciliter la collaboration au sein de l'équipe lors de l'évolution du code et de l'ajout de fonctionnalités. La base de code de la calculatrice y est reprise, documentée et testée. Les bogues sont corrigés en suivant un flux de contribution basé sur les issues, les branches et les pull requests.

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

4. Lancer l'application :

    macOS / Linux :

    ```shell
    python3 app.py
    ```

    Windows (PowerShell) :

    ```powershell
    python app.py
    ```

5. Ouvrir [http://127.0.0.1:5000](http://127.0.0.1:5000) dans un navigateur.