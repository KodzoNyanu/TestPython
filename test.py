from modulefinder import test

from flask import Flask, request, jsonify

app = Flask(__name__)

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
            
            # Ta logique pour la mention
            if note == 20:
                mention = "Excellent"
            elif note >= 16:
                mention = "Très bien"    
            elif note >= 14:
                mention = "Bien"
            elif note >= 12:
                mention = "Assez bien"
            elif note >= 10:
                mention = "Passable"
            else:
                mention = "Insuffisant"

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