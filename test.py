from modulefinder import test

from flask import Flask, request, jsonify

app = Flask(__name__)


def mention_pour_note(note):
    """Barème des mentions pour une note sur 20."""
    if note == 20:
        return "Excellent"
    elif note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"


@app.route('/api/mention')
def api_mention():
    """Endpoint JSON utilisé par l'intégration Moodle/Odoo (flux notes & mentions).

    Exemple : GET /api/mention?note=14.5 -> {"note": 14.5, "sur": 20, "mention": "Bien"}
    """
    note_saisie = request.args.get('note')
    if note_saisie is None:
        return jsonify({"erreur": "Paramètre 'note' manquant."}), 400
    try:
        note = float(note_saisie)
    except ValueError:
        return jsonify({"erreur": "La note doit être un nombre."}), 400
    if not 0 <= note <= 20:
        return jsonify({"erreur": "La note doit être comprise entre 0 et 20."}), 400
    return jsonify({"note": note, "sur": 20, "mention": mention_pour_note(note)})


@app.route('/')
# n1=1
# n2=2.3
# n3=3
# addition = n1 + n2 + n3
# multiplication = n1 * n2 * n3
# print("l'addition de n1, n2, n3 est:", addition)
# print("la multiplication de n1, n2, n3 est:", int(multiplication))
# print("la multiplication de n1, n2, n3 est:", multiplication)

# def bonjour(prenom="Philippe"):
#    # prenom = "Philippe"
#     print("Bonjour", prenom, "!", "Comment vas-tu ?")

# bonjour("Nathan")

# def calculatrice(a, b):
#     somme = a + b
#     produit = a * b
#     return somme, produit

# print("La somme et le produit de 5 et 3 sont:", calculatrice(5, 3))
# print(f"La somme et le produit de 5 et 3 sont: {calculatrice(5, 3)}")
# prix = 100.3456
# print(f"le prix est {prix:.2f} CHF")



# def boucle():
#     for i in range(5):
#         print("i=", i)

# boucle()

# print("\n")

# def boucle2():
#     i = 0
#     while i < 5:
#         print("i=", i)
#         i +=1

# boucle2()

# print("\n")

# def boucle3():
#     i = 0
#     while True:
#         print("i=", i)
#         i +=1
#         if i >= 5:
#             break

# boucle3()

# age = 25
# print(type(age))   
# print("36"+ str (36))  

# prenom = input("Quel est ton prénom ? ")

# if prenom:
#     print(f"Bonjour, je m'appelle {prenom} !")
# else:
#     print("Vous n'avez rien saisi !")



# age = int(input("Quel âge as-tu ? "))
# print(f"Je suis {prenom}, j'ai {age} ans ! et l'année prochaine j'aurai {age + 1} ans !")

# age = int(input("Quel âge as-tu ? "))
# permis = True

# if age >= 18:
#     if permis:
#         print(f"Tu as {age} ans et tu as le permis, tu peux conduire !")
#     else:
#         print(f"Tu as {age} ans mais tu n'as pas le permis, tu ne peux pas conduire !")    
# else:
#     print(f"Tu as {age} ans, tu n'as pas l'âge requis pour conduire !")


# age = int(input( "Quel âge as-tu ? " "\n"))

# if age >= 18:
#     print("Vous êtes majeur")
#     print("Bienvenue")
# print(f"Vous avez {age} ans !")
# print("Fin du programme")

def calculer_mention():
    # 1. On crée le formulaire de saisie en HTML
    html_formulaire = """
    <h1>Calculateur de Mention</h1>
    <form method="GET" action="/">
        <label for="note">Entrez votre note (sur 20) :</label>
        <input type="number" id="note" name="note" min="0" max="20" required>
        <button type="submit">Valider</button>
    </form>
    """

    # 2. On regarde si l'utilisateur a validé et envoyé une note
    note_saisie = request.args.get('note')

    if note_saisie is not None:
        try:
            note = int(note_saisie)
            mention = mention_pour_note(note)

            # On ajoute le résultat sous le formulaire
            html_resultat = f"""
            <hr>
            <h3>Résultat :</h3>
            <p>Vous avez eu {note}/20 !</p>
            <p>Votre mention est : <strong>{mention}</strong></p>
            """
            return html_formulaire + html_resultat

        except ValueError:
            html_erreur = "<p style='color:red;'>Veuillez entrer un nombre entier valide.</p>"
            return html_formulaire + html_erreur

    # Si aucune note n'a encore été saisie, on affiche juste le formulaire vide
    return html_formulaire

if __name__ == '__main__':
    app.run(debug=True)