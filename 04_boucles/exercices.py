"""Module 04 — Exercices.

Lancez avec :   python exercices.py

Certains exercices demandent d'afficher plusieurs lignes : le vérificateur les compare
une par une et vous montre la première différence.

Si un exercice ne rend jamais la main, vous avez écrit une boucle infinie :
faites Ctrl + C, puis cherchez ce qui devrait faire avancer la condition.
"""

# ---------------------------------------------------------------------------
# Exercice 1 — Compter
# Affichez les nombres de 1 à 5 inclus, un par ligne.
# Attention à range : range(5) s'arrête à 4 !
# ---------------------------------------------------------------------------
def exercice_1():
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 2 — Le compte à rebours
# Affichez 5, 4, 3, 2, 1 (un par ligne), puis « Décollage ! ».
# Faites-le avec un range à pas négatif.
# ---------------------------------------------------------------------------
def exercice_2():
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 3 — L'accumulateur
# Calculez et affichez la SOMME de tous les entiers de 1 à 100 inclus.
# Une seule ligne doit être affichée : le résultat final (5050).
# Souvenez-vous : initialiser AVANT, accumuler DEDANS, afficher APRÈS.
# ---------------------------------------------------------------------------
def exercice_3():
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 4 — La table de multiplication
# Affichez la table de `n` de 1 à 10, au format exact :
#     7 x 1 = 7
#     7 x 2 = 14
#     ...
#     7 x 10 = 70
# ---------------------------------------------------------------------------
def exercice_4(n):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 5 — Compter les voyelles
# Affichez le NOMBRE de voyelles (aeiouy, en minuscules uniquement) dans `mot`.
# Indice : `if lettre in "aeiouy":` teste si la lettre fait partie de ces
# caractères. Le mot-clé `in` sert à la fois à parcourir (dans un for) et à
# tester l'appartenance (dans un if) — deux usages bien distincts.
# ---------------------------------------------------------------------------
def exercice_5(mot):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 6 — Le premier diviseur
# Affichez le plus petit diviseur de `n` supérieur ou égal à 2.
# Pour 15 -> 3, pour 49 -> 7, pour 13 -> 13 (il est premier, il n'a que lui-même).
# Dès que vous l'avez trouvé, sortez de la boucle : ne testez pas pour rien.
# Indice : testez les candidats de 2 à n inclus.
# ---------------------------------------------------------------------------
def exercice_6(n):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 7 — FizzBuzz (le classique des entretiens d'embauche)
# Pour chaque nombre de 1 à `n` inclus, affichez :
#     « Fizz »     s'il est divisible par 3
#     « Buzz »     s'il est divisible par 5
#     « FizzBuzz » s'il est divisible par 3 ET par 5
#     le nombre    sinon
# Le piège est dans l'ORDRE des tests. Pensez au module 03 : du cas le plus
# restrictif au plus général.
# ---------------------------------------------------------------------------
def exercice_7(n):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 8 — Le triangle (boucles imbriquées)
# Pour hauteur = 4, affichez :
#     *
#     **
#     ***
#     ****
# Indice sans boucle imbriquée : "*" * 3 vaut "***" — multiplier une chaîne
# la répète. Faites-le d'abord comme ça, puis refaites-le AVEC une boucle
# imbriquée pour l'entraînement (utilisez print(..., end="") pour rester sur
# la même ligne, et un print() vide pour passer à la suivante).
# ---------------------------------------------------------------------------
def exercice_8(hauteur):
    pass  # TODO


# ---------------------------------------------------------------------------
# BONUS (non vérifié) — Le jeu du nombre mystère, dans un fichier à part.
# Tirez un nombre au hasard entre 1 et 100 :
#     import random
#     secret = random.randint(1, 100)
# Puis, avec un while, demandez des propositions à l'utilisateur jusqu'à ce
# qu'il trouve, en répondant « trop grand » ou « trop petit » à chaque essai.
# Comptez les coups et annoncez le score à la fin.
# C'est LE projet qui fait cliquer les boucles pour beaucoup de gens.
# ---------------------------------------------------------------------------


# ===========================================================================
# VÉRIFICATION — ne modifiez rien en dessous.
# ===========================================================================
import contextlib
import io


def _verifier(numero, fonction, cas):
    echecs = []
    for arguments, attendu in cas:
        tampon = io.StringIO()
        try:
            with contextlib.redirect_stdout(tampon):
                fonction(*arguments)
        except Exception as erreur:
            echecs.append(f"     {arguments} -> a planté : {erreur}")
            continue
        obtenu = tampon.getvalue().splitlines()
        if obtenu != attendu:
            echecs.append(f"     {arguments} -> attendu {attendu}")
            echecs.append(f"     {' ' * len(str(arguments))}    obtenu  {obtenu}")
    if echecs:
        print(f"RATE exercice {numero}")
        for ligne in echecs:
            print(ligne)
    else:
        print(f"OK   exercice {numero}")


if __name__ == "__main__":
    _verifier(1, exercice_1, [((), ["1", "2", "3", "4", "5"])])
    _verifier(2, exercice_2, [((), ["5", "4", "3", "2", "1", "Décollage !"])])
    _verifier(3, exercice_3, [((), ["5050"])])
    _verifier(4, exercice_4, [
        ((7,), [f"7 x {i} = {7 * i}" for i in range(1, 11)]),
        ((3,), [f"3 x {i} = {3 * i}" for i in range(1, 11)]),
    ])
    _verifier(5, exercice_5, [
        (("bonjour",), ["3"]), (("python",), ["2"]), (("xyz",), ["1"]), (("",), ["0"]),
    ])
    _verifier(6, exercice_6, [
        ((15,), ["3"]), ((49,), ["7"]), ((13,), ["13"]), ((100,), ["2"]), ((2,), ["2"]),
    ])
    _verifier(7, exercice_7, [
        ((15,), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                 "11", "Fizz", "13", "14", "FizzBuzz"]),
        ((3,), ["1", "2", "Fizz"]),
    ])
    _verifier(8, exercice_8, [
        ((4,), ["*", "**", "***", "****"]),
        ((1,), ["*"]),
    ])
