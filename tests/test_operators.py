"""Tests des fonctions de calcul de operators.py.

Chaque opération est testée seule, sans passer par l'analyse de l'expression,
pour qu'un échec pointe directement vers la fonction fautive.
"""

import pytest

from operators import add, subtract, multiply, divide


def test_add():
    """Vérifie que add() retourne la somme des deux nombres."""
    assert add(5, 3) == 8


def test_subtract():
    """Vérifie que subtract() soustrait le deuxième nombre du premier."""
    assert subtract(5, 3) == 2


def test_multiply():
    """Vérifie que multiply() retourne le produit des deux nombres."""
    assert multiply(2, 3) == 6


def test_divide():
    """Vérifie que divide() fait une division décimale."""
    assert divide(7, 2) == 3.5


def test_divide_par_zero():
    """Vérifie que divide() lève une erreur pour une division par zéro."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)