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
    # On récupère la note passée dans l'URL (ex: /?note=14). Si rien n'est mis, on prend 10 par défaut.
    try:
        note = int(request.args.get('note', 10))
    except ValueError:
        return "Veuillez entrer un nombre entier valide pour la note. Exemple : /?note=14"

    # Ton code de logique pour la mention
    if note >= 14:
        mention = "Bien"
    elif note >= 12:
        mention = "Assez bien"
    elif note >= 10:
        mention = "Passable"
    else:
        mention = "Insuffisant"

    # On affiche le résultat proprement sur la page web
    return f"<h1>Résultat</h1><p>Vous avez eu {note}/20 !</p><p>Votre mention est : <strong>{mention}</strong></p>"

if __name__ == '__main__':
    app.run(debug=True)