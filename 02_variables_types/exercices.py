"""Module 02 — Exercices.

Lancez avec :   python exercices.py

Rappel : `def exercice_N():` est juste une étiquette (module 06 pour les détails).
Écrivez vos lignes en dessous, décalées de 4 espaces, et supprimez le `pass`.
"""

# ---------------------------------------------------------------------------
# Exercice 1 — Vos premières variables
# Créez trois variables, directement ici (pas dans une fonction) :
#   - ville     : le texte  Paris
#   - habitants : le nombre entier 2 100 000  (écrivez 2100000, sans espace !)
#   - densite   : le nombre à virgule 20641.0
# ---------------------------------------------------------------------------
ville = "Paris"       
habitants = 2100000   
densite = 20641.0      


# ---------------------------------------------------------------------------
# Exercice 2 — Le compteur
# En partant de 0, faites passer `score` à 30, en TROIS lignes de +10,
# en utilisant le raccourci += à chaque fois.
# ---------------------------------------------------------------------------
score = 0
score += 10
score += 10
score += 10


# ---------------------------------------------------------------------------
# Exercice 3 — Une f-string
# En utilisant les variables `ville` et `habitants` de l'exercice 1, affichez :
#     Paris compte 2100000 habitants
# Utilisez une f-string, pas des + ni des virgules.
# ---------------------------------------------------------------------------
def exercice_3():
    print(f"{ville} compte {habitants} habitants ")


# ---------------------------------------------------------------------------
# Exercice 4 — Conversion
# La variable `saisie` ci-dessous contient du TEXTE (comme si elle venait d'un
# input()). Convertissez-la en entier, ajoutez-lui 8, et affichez le résultat.
# Attendu :   42
# ---------------------------------------------------------------------------
saisie = "34"


def exercice_4():
   saisie = int(input("Entrez un nombre : "))
   print(saisie + 8)


# ---------------------------------------------------------------------------
# Exercice 5 — Quotient et reste
# 100 secondes, ça fait combien de minutes et combien de secondes ?
# Avec // et %, affichez exactement :   1 min 40 s
# ---------------------------------------------------------------------------
def exercice_5():
    secondes = 100
    minutes = secondes // 60
    reste_secondes = secondes % 60
    print(f"{minutes} min {reste_secondes} s")

# ---------------------------------------------------------------------------
# Exercice 6 — Le prix TTC
# Le prix hors taxes est 19.99 et la TVA est de 20 % (donc x 1.2).
# Calculez le prix TTC et affichez-le arrondi à 2 décimales, suivi de " EUR".
# Attendu :   23.99 EUR
# (Indice : le format {valeur:.2f} dans une f-string.)
# ---------------------------------------------------------------------------
prix_ht = 19.99
taux_tva = 1.2


def exercice_6():
    prix_ttc = prix_ht * taux_tva
    print(f"{prix_ttc:.2f} EUR")



# ---------------------------------------------------------------------------
# Exercice 7 — Échanger deux variables
# Faites en sorte qu'après votre code, `a` vaille 2 et `b` vaille 1.
# Attention : `a = b` puis `b = a` NE MARCHE PAS — réfléchissez à pourquoi
# (que vaut a après la première ligne ? et donc que copie la seconde ?).
# Indice : une troisième variable temporaire résout le problème.
# ---------------------------------------------------------------------------
a = 1
b = 2
temp = a
a = b
b = temp


# ---------------------------------------------------------------------------
# BONUS (non vérifié) — Écrivez un petit programme interactif dans un fichier
# à part : demandez son prénom et son année de naissance à l'utilisateur avec
# input(), puis affichez « Bonjour X, tu as (ou tu auras) N ans en 2026 ».
# N'oubliez pas la conversion !
# ---------------------------------------------------------------------------

prenom = input("Quel est ton prénom ? ")
print(f"Bonjour, je m'appelle {prenom} !")

age = int(input("Quel âge as-tu ? "))
print(f"J'ai {age} ans ! et l'année prochaine j'aurai {age + 1} ans !")
# ===========================================================================
# VÉRIFICATION — ne modifiez rien en dessous.
# ===========================================================================
import contextlib
import io


def _verifier_valeur(nom, obtenu, attendu):
    if obtenu == attendu and type(obtenu) is type(attendu):
        print(f"OK   {nom}")
    else:
        print(f"RATE {nom} : attendu {attendu!r} ({type(attendu).__name__}), "
              f"obtenu {obtenu!r} ({type(obtenu).__name__})")


def _verifier_sortie(numero, fonction, lignes_attendues):
    tampon = io.StringIO()
    try:
        with contextlib.redirect_stdout(tampon):
            fonction()
    except Exception as erreur:
        print(f"RATE exercice {numero} : votre code a planté -> {erreur}")
        return
    obtenu = tampon.getvalue().splitlines()
    if obtenu == lignes_attendues:
        print(f"OK   exercice {numero}")
    else:
        print(f"RATE exercice {numero}")
        print(f"     attendu : {lignes_attendues}")
        print(f"     obtenu  : {obtenu}")


if __name__ == "__main__":
    _verifier_valeur("exercice 1 (ville)", ville, "Paris")
    _verifier_valeur("exercice 1 (habitants)", habitants, 2100000)
    _verifier_valeur("exercice 1 (densite)", densite, 20641.0)
    _verifier_valeur("exercice 2 (score)", score, 30)
    _verifier_sortie(3, exercice_3, ["Paris compte 2100000 habitants"])
    _verifier_sortie(4, exercice_4, ["42"])
    _verifier_sortie(5, exercice_5, ["1 min 40 s"])
    _verifier_sortie(6, exercice_6, ["23.99 EUR"])
    _verifier_valeur("exercice 7 (a)", a, 2)
    _verifier_valeur("exercice 7 (b)", b, 1)
