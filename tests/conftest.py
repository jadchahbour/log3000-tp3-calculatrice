"""Configuration commune aux tests.

pytest charge ce fichier automatiquement. Les fixtures définies ici sont
disponibles dans tous les fichiers de test sans avoir à les importer.
"""

import pytest

from app import app


@pytest.fixture
def client():
    """Fournit un client de test Flask.

    Le client simule un navigateur : il envoie des requêtes à l'application
    sans lancer de vrai serveur.

    Yields:
        FlaskClient: Client utilisé pour envoyer des requêtes GET et POST.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client