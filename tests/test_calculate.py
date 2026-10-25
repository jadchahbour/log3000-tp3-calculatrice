"""Tests de la fonction calculate() de app.py.

Ces tests vérifient l'analyse de l'expression (découpage, validation) et le
résultat final du calcul.
"""

import pytest

from app import calculate


def test_addition():
    """Vérifie le calcul d'une addition."""
    assert calculate("2+3") == 5


def test_soustraction():
    """Vérifie le calcul d'une soustraction."""
    assert calculate("9-5") == 4


def test_multiplication():
    """Vérifie le calcul d'une multiplication."""
    assert calculate("4*3") == 12


def test_division():
    """Vérifie le calcul d'une division avec un résultat décimal."""
    assert calculate("9/2") == 4.5


def test_espaces_ignores():
    """Vérifie que les espaces dans l'expression sont ignorés."""
    assert calculate(" 2 + 3 ") == 5


def test_expression_vide():
    """Vérifie qu'une expression vide est refusée."""
    with pytest.raises(ValueError):
        calculate("")


def test_sans_operateur():
    """Vérifie qu'une expression sans opérateur est refusée."""
    with pytest.raises(ValueError):
        calculate("5")


def test_plusieurs_operateurs():
    """Vérifie qu'une expression avec plus d'un opérateur est refusée."""
    with pytest.raises(ValueError):
        calculate("2+3+4")


def test_operateur_au_debut():
    """Vérifie qu'un opérateur en première position est refusé."""
    with pytest.raises(ValueError):
        calculate("+5")


def test_operateur_a_la_fin():
    """Vérifie qu'un opérateur en dernière position est refusé."""
    with pytest.raises(ValueError):
        calculate("5+")


def test_nombre_negatif_refuse():
    """Vérifie qu'un nombre négatif est refusé, car il n'est pas pris en charge."""
    with pytest.raises(ValueError):
        calculate("-5+3")


def test_division_par_zero():
    """Vérifie qu'une division par zéro lève une erreur."""
    with pytest.raises(ZeroDivisionError):
        calculate("5/0")