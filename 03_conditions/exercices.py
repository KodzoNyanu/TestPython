"""Module 03 — Exercices.

Lancez avec :   python exercices.py

NOUVEAUTÉ dans les étiquettes : `def exercice_1(age):` — l'étiquette reçoit maintenant
une valeur. Le vérificateur appellera votre code plusieurs fois avec des valeurs
différentes (18, 12, 17...) pour tester tous les cas. À l'intérieur, servez-vous
simplement de `age` comme d'une variable normale ; elle contiendra la valeur du test
en cours. Tout s'expliquera au module 06.
"""

# ---------------------------------------------------------------------------
# Exercice 1 — Majeur ou mineur
# Affichez « Majeur » si age vaut 18 ou plus, « Mineur » sinon.
# ---------------------------------------------------------------------------
def exercice_1(age):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 2 — Les mentions
# Affichez la mention correspondant à la note :
#     >= 16          Très bien
#     >= 14          Bien
#     >= 12          Assez bien
#     >= 10          Passable
#     en dessous     Insuffisant
# Attention à l'ORDRE de vos elif.
# ---------------------------------------------------------------------------
def exercice_2(note):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 3 — Pair, impair, zéro
# Affichez « zéro » si nombre vaut 0, sinon « pair » ou « impair ».
# (Indice : le modulo % du module 02.)
# ---------------------------------------------------------------------------
def exercice_3(nombre):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 4 — Le permis
# Affichez :
#     « Peut conduire »          si majeur (18+) ET titulaire du permis
#     « Majeur sans permis »     si majeur mais sans permis
#     « Trop jeune »             si mineur (avec ou sans permis)
# `permis` est un booléen : écrivez `if permis:`, pas `if permis == True:`.
# ---------------------------------------------------------------------------
def exercice_4(age, permis):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 5 — Saisie vide
# `prenom` contient ce qu'aurait renvoyé un input(), donc parfois du vide.
# Affichez « Bonjour X ! » si un prénom est renseigné, « Vous n'avez rien tapé »
# si la chaîne est vide. Utilisez le fait qu'une chaîne vide est « fausse ».
# ---------------------------------------------------------------------------
def exercice_5(prenom):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 6 — Note valide
# Affichez « valide » si la note est entre 0 et 20 inclus, « invalide » sinon.
# Utilisez la comparaison enchaînée, à la manière des maths.
# ---------------------------------------------------------------------------
def exercice_6(note):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 7 — Les années bissextiles (le plus dur du module, prenez le temps)
# Une année est bissextile si :
#     - elle est divisible par 4,
#     - SAUF si elle est divisible par 100,
#     - MAIS elle l'est quand même si elle est divisible par 400.
# Ainsi : 2024 oui, 1900 non (divisible par 100), 2000 oui (divisible par 400).
# Affichez « bissextile » ou « commune ».
# Deux approches marchent : plusieurs if imbriqués, ou une seule condition avec
# and / or / not. Essayez la première si la seconde vous résiste.
# ---------------------------------------------------------------------------
def exercice_7(annee):
    pass  # TODO


# ---------------------------------------------------------------------------
# BONUS (non vérifié) — Dans un fichier à part, un mini quiz : posez une question
# avec input(), comparez la réponse à la bonne, et félicitez ou corrigez.
# Astuce pour être tolérant : `if reponse.lower() == "paris":` met la saisie en
# minuscules avant de comparer, ce qui accepte « PARIS » et « Paris ».
# ---------------------------------------------------------------------------


# ===========================================================================
# VÉRIFICATION — ne modifiez rien en dessous.
# ===========================================================================
import contextlib
import io


def _verifier(numero, fonction, cas):
    """cas : liste de (arguments, sortie_attendue)."""
    echecs = []
    for arguments, attendu in cas:
        tampon = io.StringIO()
        try:
            with contextlib.redirect_stdout(tampon):
                fonction(*arguments)
        except Exception as erreur:
            echecs.append(f"     {arguments} -> a planté : {erreur}")
            continue
        obtenu = tampon.getvalue().strip()
        if obtenu != attendu:
            echecs.append(f"     {arguments} -> attendu {attendu!r}, obtenu {obtenu!r}")
    if echecs:
        print(f"RATE exercice {numero}")
        for ligne in echecs:
            print(ligne)
    else:
        print(f"OK   exercice {numero}")


if __name__ == "__main__":
    _verifier(1, exercice_1, [
        ((18,), "Majeur"), ((25,), "Majeur"), ((17,), "Mineur"), ((0,), "Mineur"),
    ])
    _verifier(2, exercice_2, [
        ((20,), "Très bien"), ((16,), "Très bien"), ((15,), "Bien"), ((14,), "Bien"),
        ((13,), "Assez bien"), ((10,), "Passable"), ((9.5,), "Insuffisant"), ((0,), "Insuffisant"),
    ])
    _verifier(3, exercice_3, [
        ((0,), "zéro"), ((4,), "pair"), ((7,), "impair"), ((100,), "pair"),
    ])
    _verifier(4, exercice_4, [
        ((20, True), "Peut conduire"), ((20, False), "Majeur sans permis"),
        ((15, False), "Trop jeune"), ((15, True), "Trop jeune"),
    ])
    _verifier(5, exercice_5, [
        (("Ada",), "Bonjour Ada !"), (("",), "Vous n'avez rien tapé"),
    ])
    _verifier(6, exercice_6, [
        ((0,), "valide"), ((20,), "valide"), ((12,), "valide"),
        ((-1,), "invalide"), ((21,), "invalide"),
    ])
    _verifier(7, exercice_7, [
        ((2024,), "bissextile"), ((2023,), "commune"), ((1900,), "commune"),
        ((2000,), "bissextile"), ((2100,), "commune"), ((1600,), "bissextile"),
    ])
