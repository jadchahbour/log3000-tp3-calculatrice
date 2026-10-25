# Tests

## Exécuter les tests

1. Installer pytest :

    ```shell
    pip install pytest
    ```

2. Lancer tous les tests depuis la racine du projet :

    ```shell
    pytest
    ```

## Ce que couvrent les tests

- `test_operators.py` : les fonctions de calcul de `backend/operators.py` (addition, soustraction, multiplication et division). Il teste aussi la division par zéro.
- `test_calculate.py` : la fonction `calculate()` de `backend/app.py`, Il teste les 4 opérations possibles. Il teste aussi les expressions invalides (expression vide, expression ne contenant aucun ou plusieurs opérateur, expression avec opérateur au début ou à la fin, nombre négatif, division par zéro).
- `test_interface.py` : Ce module teste la page de la calculatrice. Il vérifie que la page s'affiche et que le résultat ou le message d'erreur apparaît à l'écran après un calcul. Finalement, il vérifie aussi que chaque bouton affiche la valeur qu'il ajoute à l'écran.