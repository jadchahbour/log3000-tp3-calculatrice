"""Serveur Flask de la calculatrice.

Ce module lance l'application web, affiche l'interface et reçoit les
expressions envoyées par le formulaire HTML. L'expression est analysée par la
fonction calculate(). Le calcul est ensuite délégué aux fonctions du module
operators.py, selon l'opérateur utilisé.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Crée l'application Flask. Les dossiers templates et static sont à la racine
# du projet, d'où les chemins relatifs.
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Associe chaque symbole d'opérateur à sa fonction. Ce dictionnaire évite un long
# if/elif ou un switch. Il permet d'ajouter un nouveau opérateur sans toucher calculate().
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Évalue une expression contenant une seule opération entre 2 nombres.

    Args:
        expr (str): Expression à évaluer, par exemple "9-5".

    Returns:
        float: Le résultat de l'opération.

    Raises:
        ValueError: Si l'expression est vide, ne contient aucun ou plusieurs
            opérateurs, commence ou finit par un opérateur, ou si les opérandes ne
            sont pas des nombres.
        ZeroDivisionError: Si l'expression demande une division par zéro.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    # -1 indique qu'aucun opérateur n'a encore été trouvé.
    op_pos = -1
    op_char = None

    # Les nombres négatifs ne sont pas pris en charge par la calculatrice,
    # car ils ajoutent un opérateur de plus (à cause du signe "-") et
    # l'expression est rejetée.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Un opérateur en première ou dernière position signifie qu'il manque
    # un opérande. Une position de -1 signifie qu'aucun opérateur n'est présent.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Découpe l'expression de part et d'autre de l'opérateur.
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et traite les calculs envoyés par le formulaire
    HTML.

    Une requête GET affiche la page avec une saisie d'expression vide.
    Une requête POST récupère l'expression du champ display, la calcule et
    renvoie la page avec le résultat ou le message d'erreur.

    Returns:
        str: La page HTML de la calculatrice.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Toute erreur est affichée à l'écran grâce à ce bloc,
            # ce qui permet de ne jamais planter la page.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Le mode debug recharge le serveur à chaque modification du code.
    app.run(debug=True)