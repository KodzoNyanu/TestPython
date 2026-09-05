"""Module 01 — Exercices.

Lancez ce fichier avec :   python exercices.py

Au premier lancement, tout est marqué RATE : c'est normal, rien n'est écrit.
Complétez les zones marquées TODO, relancez, et visez le plein OK.

UNE SEULE CHOSE À ACCEPTER POUR L'INSTANT :
chaque exercice commence par une ligne du genre `def exercice_1():`. C'est une étiquette
qui permet au vérificateur, en bas du fichier, de retrouver votre code. On expliquera
tout ça au module 06 — pour l'instant, écrivez simplement vos lignes EN DESSOUS, décalées
de 4 espaces vers la droite. Ce décalage n'est pas décoratif : en Python, c'est lui qui
dit « ces lignes appartiennent à l'exercice ». Supprimez le `pass` quand vous écrivez
votre code (`pass` veut dire « ici, ne rien faire »).
"""

# ---------------------------------------------------------------------------
# Exercice 1 — Le grand classique
# Affichez exactement :   Bonjour le monde !
# ---------------------------------------------------------------------------
def exercice_1():
    print("Bonjour le monde !")


# ---------------------------------------------------------------------------
# Exercice 2 — Plusieurs lignes
# Affichez trois lignes, dans cet ordre :
#     Je m'appelle Ada
#     J'apprends Python
#     Et ça commence bien
# Attention à l'apostrophe de « J'apprends » : choisissez bien vos guillemets.
# ---------------------------------------------------------------------------
def exercice_2():
    print("Je m'appelle Ada")
    print("J'apprends Python")
    print("Et ça commence bien")


# ---------------------------------------------------------------------------
# Exercice 3 — Plusieurs arguments
# En UN SEUL appel à print, avec TROIS arguments séparés par des virgules,
# affichez :   Python est genial
# (Rappel : print insère automatiquement une espace entre les arguments.)
# ---------------------------------------------------------------------------
def exercice_3():
    print("Python", "est", "genial")


# ---------------------------------------------------------------------------
# Exercice 4 — Les guillemets dans le texte
# Affichez exactement, guillemets compris :   Elle a dit "bonjour" puis elle est partie
# ---------------------------------------------------------------------------
def exercice_4():
    print('Elle a dit "bonjour" puis elle est partie')


# ---------------------------------------------------------------------------
# Exercice 5 — Un commentaire utile
# Affichez le résultat du calcul 7 * 6 (sans guillemets autour : c'est un calcul,
# pas du texte !), et ajoutez au-dessus un commentaire qui explique POURQUOI ce
# nombre, pas ce que fait la ligne.
# ---------------------------------------------------------------------------
def exercice_5():
    # le nombre 42 est le résultat de 7 * 6
    print(7 * 5)


# ---------------------------------------------------------------------------
# BONUS (non vérifié) — Provoquez une erreur volontairement.
# Dans un fichier à part, écrivez `print("test"` sans parenthèse fermante,
# lancez-le, et lisez le message. Repérez : la dernière ligne (le problème),
# le nom du fichier et le numéro de ligne (l'endroit), et le petit ^.
# ---------------------------------------------------------------------------

print("test")
# ===========================================================================
# VÉRIFICATION — ne modifiez rien en dessous de cette ligne.
# ===========================================================================
import contextlib
import io


def _verifier(numero, fonction, lignes_attendues):
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
    _verifier(1, exercice_1, ["Bonjour le monde !"])
    _verifier(2, exercice_2, ["Je m'appelle Ada", "J'apprends Python", "Et ça commence bien"])
    _verifier(3, exercice_3, ["Python est genial"])
    _verifier(4, exercice_4, ['Elle a dit "bonjour" puis elle est partie'])
    _verifier(5, exercice_5, ["42"])
