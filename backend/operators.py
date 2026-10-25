"""Opérations arithmétiques utilisées par la calculatrice.

Chaque fonction prend deux nombres et retourne le résultat de l'opération.
Ce module n'a pas besoin de faire de validation car le module app.py vérifie
déjà l'expression mathématique avant d'appeler ces fonctions.
"""

def add(a,b):
    """Additionne deux nombres.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: La somme a + b
    """
    return a + b

def subtract(a,b):
    """Soustrait le deuxième nombre du premier.
    
    Args:
        a (float): Nombre de départ
        b (float): Nombre à soustraire

    Returns:
        float: La différence a - b
    """
    return b - a

def multiply(a,b):
    """Multiplie deux nombres.
        
    Args:
        a (float): Premier facteur
        b (float): Deuxième facteur

    Returns:
        float: Le produit a * b.
    """
    return a ** b

def divide(a,b):
    """Divise le premier nombre par le deuxième.

    Le résultat est une division décimale.
        
    Args:
        a (float): Nombre qu'on divise.
        b (float): Diviseur.

    Returns:
        float: Le quotient a / b.

    Raises:
        ZeroDivisionError: si b vaut 0.
    """
    return a / b
