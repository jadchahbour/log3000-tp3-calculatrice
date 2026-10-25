"""Tests de la page de la calculatrice.

Ces tests passent par le client de test Flask : ils vérifient la page HTML
renvoyée au navigateur, comme le verrait un utilisateur.
"""

import re


def test_page_accessible(client):
    """Vérifie que la page principale s'affiche avec son champ d'écran.

    Args:
        client: Client de test Flask (fixture de conftest.py).
    """
    response = client.get("/")
    assert response.status_code == 200
    assert 'name="display"' in response.text


def test_resultat_decimal_affiche(client):
    """Vérifie qu'un résultat décimal s'affiche à l'écran.

    Args:
        client: Client de test Flask (fixture de conftest.py).
    """
    response = client.post("/", data={"display": "9/2"})
    assert 'value="4.5"' in response.text


def test_message_erreur_affiche(client):
    """Vérifie qu'une expression invalide affiche un message d'erreur.

    Args:
        client: Client de test Flask (fixture de conftest.py).
    """
    response = client.post("/", data={"display": "2+3+4"})
    assert 'value="Error:' in response.text


def test_libelles_des_boutons(client):
    """Vérifie que chaque bouton affiche la valeur qu'il ajoute à l'écran.

    Args:
        client: Client de test Flask (fixture de conftest.py).
    """
    response = client.get("/")
    # Récupère chaque paire (valeur ajoutée, texte affiché) des boutons de saisie.
    boutons = re.findall(r"appendToDisplay\('(.)'\)\">(.*?)</button>", response.text)
    erreurs = [f"bouton '{valeur}' affiche '{texte}'"
               for valeur, texte in boutons if texte != valeur]
    assert not erreurs, ", ".join(erreurs)