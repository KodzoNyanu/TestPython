"""Module 06 — Exercices.

Lancez avec :   python exercices.py

CHANGEMENT IMPORTANT : à partir de ce module, les exercices ne sont plus des
« étiquettes ». Ce sont de vraies fonctions, et le vérificateur teste ce qu'elles
RENVOIENT (return), pas ce qu'elles affichent. Un print à la place d'un return
donnera systématiquement None — c'est le piège du module, et il est volontaire.
"""


# ---------------------------------------------------------------------------
# Exercice 1 — return, pas print
# Renvoyez le carré du nombre reçu.
# ---------------------------------------------------------------------------
def carre(nombre):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 2 — Plusieurs paramètres
# Renvoyez le prix TTC à partir du prix HT et d'un taux de TVA en décimal
# (0.2 = 20 %). Le taux doit valoir 0.2 PAR DÉFAUT, donc calculer_ttc(100)
# doit fonctionner seul et renvoyer 120.0.
# ---------------------------------------------------------------------------
def calculer_ttc(prix_ht, taux=None):   # TODO: corrigez la valeur par défaut
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 3 — return et condition
# Renvoyez la valeur absolue du nombre, SANS utiliser abs().
# Souvenez-vous que return sort immédiatement de la fonction : vous n'avez
# pas besoin de else.
# ---------------------------------------------------------------------------
def valeur_absolue(nombre):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 4 — Renvoyer un booléen
# Renvoyez True si l'année est bissextile, False sinon.
# (Même règle qu'au module 03 : divisible par 4, sauf par 100, sauf par 400.)
# Écrivez `return (la condition)` directement : une comparaison EST déjà un
# booléen, inutile d'écrire `if condition: return True else: return False`.
# ---------------------------------------------------------------------------
def est_bissextile(annee):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 5 — Renvoyer un texte
# Renvoyez la mention correspondant à la note (mêmes seuils qu'au module 03 :
# 16 Très bien, 14 Bien, 12 Assez bien, 10 Passable, sinon Insuffisant).
# ---------------------------------------------------------------------------
def mention(note):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 6 — Renvoyer une liste
# Renvoyez la liste des nombres pairs de la liste reçue, dans le même ordre.
#     [1, 2, 3, 4] -> [2, 4]
# Attention : ne modifiez pas la liste reçue, construisez-en une nouvelle.
# ---------------------------------------------------------------------------
def garder_pairs(nombres):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 7 — Le cas vide
# Renvoyez la moyenne de la liste de notes, arrondie à 2 décimales (round(x, 2)).
# MAIS : si la liste est vide, renvoyez None au lieu de planter.
# Réfléchissez : que vaut sum([]) / len([]) ? Essayez dans un terminal python.
# Traiter les cas limites AVANT le cas normal est un réflexe de professionnel.
# ---------------------------------------------------------------------------
def moyenne(notes):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 8 — Composer des fonctions
# Renvoyez un dictionnaire résumant les notes :
#     {"moyenne": 13.88, "mention": "Assez bien", "reussi": True}
# « reussi » vaut True si la moyenne atteint 10.
# Contrainte : RÉUTILISEZ vos fonctions moyenne() et mention(). Ne recopiez
# aucun calcul — c'est tout l'intérêt d'avoir découpé.
# Si la liste est vide, renvoyez None.
# ---------------------------------------------------------------------------
def bulletin(notes):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 9 — La docstring
# Écrivez une fonction qui renvoie le plus grand des trois nombres reçus,
# SANS max(). Elle doit avoir une docstring en première ligne (une chaîne
# entre triples guillemets qui dit ce que fait la fonction).
# ---------------------------------------------------------------------------
def plus_grand(a, b, c):
    pass  # TODO


# ---------------------------------------------------------------------------
# BONUS (non vérifié) — Reprenez le jeu du nombre mystère du module 04 et
# réécrivez-le en fonctions : tirer_secret(), demander_proposition(),
# comparer(proposition, secret) qui renvoie "trop grand"/"trop petit"/"gagné",
# et jouer() qui orchestre le tout. Le même programme, mais lisible.
# ---------------------------------------------------------------------------


# ===========================================================================
# VÉRIFICATION — ne modifiez rien en dessous.
# ===========================================================================
def _verifier(nom, fonction, cas):
    echecs = []
    for arguments, attendu in cas:
        try:
            obtenu = fonction(*arguments)
        except Exception as erreur:
            echecs.append(f"     {arguments} -> a planté : {type(erreur).__name__} {erreur}")
            continue
        if obtenu != attendu or type(obtenu) is not type(attendu):
            indice = ""
            if obtenu is None and attendu is not None:
                indice = "   (None = vous avez sans doute fait print au lieu de return)"
            echecs.append(f"     {arguments} -> attendu {attendu!r}, obtenu {obtenu!r}{indice}")
    if echecs:
        print(f"RATE {nom}")
        for ligne in echecs:
            print(ligne)
    else:
        print(f"OK   {nom}")


if __name__ == "__main__":
    _verifier("exercice 1 (carre)", carre, [((4,), 16), ((-3,), 9), ((0,), 0)])
    _verifier("exercice 2 (calculer_ttc)", calculer_ttc, [
        ((100,), 120.0), ((100, 0.055), 105.5), ((0,), 0.0),
    ])
    _verifier("exercice 3 (valeur_absolue)", valeur_absolue, [
        ((5,), 5), ((-5,), 5), ((0,), 0),
    ])
    _verifier("exercice 4 (est_bissextile)", est_bissextile, [
        ((2024,), True), ((2023,), False), ((1900,), False), ((2000,), True),
    ])
    _verifier("exercice 5 (mention)", mention, [
        ((18,), "Très bien"), ((14,), "Bien"), ((12,), "Assez bien"),
        ((10,), "Passable"), ((5,), "Insuffisant"),
    ])
    _verifier("exercice 6 (garder_pairs)", garder_pairs, [
        (([1, 2, 3, 4],), [2, 4]), (([1, 3],), []), (([],), []),
    ])
    _verifier("exercice 7 (moyenne)", moyenne, [
        (([12, 15.5, 8, 20],), 13.88), (([10],), 10.0), (([],), None),
    ])
    _verifier("exercice 8 (bulletin)", bulletin, [
        (([12, 15.5, 8, 20],), {"moyenne": 13.88, "mention": "Assez bien", "reussi": True}),
        (([5, 6],), {"moyenne": 5.5, "mention": "Insuffisant", "reussi": False}),
        (([],), None),
    ])
    _verifier("exercice 9 (plus_grand)", plus_grand, [
        ((1, 2, 3), 3), ((3, 2, 1), 3), ((1, 3, 2), 3), ((5, 5, 5), 5), ((-1, -2, -3), -1),
    ])
    if plus_grand.__doc__:
        print("OK   exercice 9 (docstring)")
    else:
        print("RATE exercice 9 (docstring) : il manque la chaîne de documentation")
