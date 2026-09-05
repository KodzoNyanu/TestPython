"""Module 05 — Exercices.

Lancez avec :   python exercices.py
"""

# ---------------------------------------------------------------------------
# Exercice 1 — Manipuler une liste
# En partant de la liste ci-dessous, et SANS la réécrire à la main, obtenez :
#     ["banane", "cerise", "datte", "fraise"]
# Il vous faut : supprimer "abricot", ajouter "fraise" à la fin, et trier.
# (Le tri alphabétique remettra tout dans l'ordre, ne vous en souciez pas.)
# ---------------------------------------------------------------------------
fruits = ["cerise", "abricot", "banane", "datte"]
# TODO: vos lignes ici


# ---------------------------------------------------------------------------
# Exercice 2 — Statistiques
# Affichez trois lignes, en utilisant les fonctions toutes faites du cours
# (aucune boucle n'est nécessaire) :
#     Moyenne : 13.88
#     Minimum : 8
#     Maximum : 20
# La moyenne est arrondie à 2 décimales à l'affichage.
# ---------------------------------------------------------------------------
def exercice_2(notes):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 3 — Le classement numéroté
# Affichez la liste avec un numéro qui commence à 1 :
#     1. Ada
#     2. Alan
#     3. Grace
# Utilisez enumerate.
# ---------------------------------------------------------------------------
def exercice_3(prenoms):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 4 — Les premiers et les derniers
# Avec du découpage (slicing), affichez sur trois lignes :
#     les 2 premiers éléments de la liste
#     les 2 derniers
#     la liste à l'envers
# Affichez les listes telles quelles : print(ma_liste) suffit.
# Indice pour l'envers : le pas de -1 marche aussi en slicing -> [::-1].
# ---------------------------------------------------------------------------
def exercice_4(nombres):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 5 — Une fiche
# `personne` est un dictionnaire qui contient au moins "prenom" et "age",
# mais PAS TOUJOURS "ville". Affichez :
#     Ada, 36 ans, Londres
# et si la ville est absente, affichez « ville inconnue » à sa place.
# Le programme ne doit jamais planter : pensez à get.
# ---------------------------------------------------------------------------
def exercice_5(personne):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 6 — Compter les occurrences
# Comptez combien de fois chaque mot apparaît, puis affichez une ligne par mot,
# TRIÉE par ordre alphabétique du mot :
#     chat : 3
#     chien : 1
#     oiseau : 1
# Indice pour le tri : `for mot in sorted(comptes):` parcourt les clés triées.
# ---------------------------------------------------------------------------
def exercice_6(mots):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 7 — Le total des dépenses
# `depenses` est une liste de dictionnaires ayant les clés "libelle" et "montant".
# Affichez une ligne par dépense, puis le total :
#     Café : 2.50 €
#     Train : 45.00 €
#     Total : 47.50 €
# (Tous les montants ont 2 décimales à l'affichage.)
# ---------------------------------------------------------------------------
def exercice_7(depenses):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 8 — Le total PAR CATÉGORIE (l'exercice le plus important du module)
# Chaque dépense a aussi une clé "categorie". Affichez le total par catégorie,
# trié par nom de catégorie :
#     loisirs : 18.90 €
#     sorties : 2.50 €
#     transport : 45.00 €
# C'est la combinaison de deux motifs déjà vus : le dictionnaire compteur du
# cours, et l'accumulateur du module 04. Ici on n'accumule pas des 1 mais des
# montants — et on ne le fait pas dans une variable mais dans un dictionnaire.
# Ce calcul, en data, s'appelle un « group by ». Vous le referez toute votre vie.
# ---------------------------------------------------------------------------
def exercice_8(depenses):
    pass  # TODO


# ---------------------------------------------------------------------------
# BONUS (non vérifié) — Reprenez le compteur de voyelles du module 04 et
# transformez-le : au lieu du nombre total, affichez le détail par voyelle
# ({"o": 2, "u": 1}...). Puis affichez la voyelle la plus fréquente.
# ---------------------------------------------------------------------------


# ===========================================================================
# VÉRIFICATION — ne modifiez rien en dessous.
# ===========================================================================
import contextlib
import io


def _verifier_valeur(nom, obtenu, attendu):
    if obtenu == attendu:
        print(f"OK   {nom}")
    else:
        print(f"RATE {nom} : attendu {attendu!r}, obtenu {obtenu!r}")


def _verifier(numero, fonction, cas):
    echecs = []
    for arguments, attendu in cas:
        tampon = io.StringIO()
        try:
            with contextlib.redirect_stdout(tampon):
                fonction(*arguments)
        except Exception as erreur:
            echecs.append(f"     a planté sur {arguments} : {type(erreur).__name__} {erreur}")
            continue
        obtenu = tampon.getvalue().splitlines()
        if obtenu != attendu:
            echecs.append(f"     attendu : {attendu}")
            echecs.append(f"     obtenu  : {obtenu}")
    if echecs:
        print(f"RATE exercice {numero}")
        for ligne in echecs:
            print(ligne)
    else:
        print(f"OK   exercice {numero}")


_DEPENSES = [
    {"libelle": "Café", "montant": 2.5, "categorie": "sorties"},
    {"libelle": "Train", "montant": 45.0, "categorie": "transport"},
    {"libelle": "Livre", "montant": 18.9, "categorie": "loisirs"},
]

if __name__ == "__main__":
    _verifier_valeur("exercice 1 (fruits)", fruits, ["banane", "cerise", "datte", "fraise"])
    _verifier(2, exercice_2, [
        (([12, 15.5, 8, 20],), ["Moyenne : 13.88", "Minimum : 8", "Maximum : 20"]),
    ])
    _verifier(3, exercice_3, [
        ((["Ada", "Alan", "Grace"],), ["1. Ada", "2. Alan", "3. Grace"]),
    ])
    _verifier(4, exercice_4, [
        (([0, 1, 2, 3, 4, 5],), ["[0, 1]", "[4, 5]", "[5, 4, 3, 2, 1, 0]"]),
    ])
    _verifier(5, exercice_5, [
        (({"prenom": "Ada", "age": 36, "ville": "Londres"},), ["Ada, 36 ans, Londres"]),
        (({"prenom": "Alan", "age": 41},), ["Alan, 41 ans, ville inconnue"]),
    ])
    _verifier(6, exercice_6, [
        ((["chat", "chien", "chat", "oiseau", "chat"],),
         ["chat : 3", "chien : 1", "oiseau : 1"]),
    ])
    _verifier(7, exercice_7, [
        ((_DEPENSES[:2],), ["Café : 2.50 €", "Train : 45.00 €", "Total : 47.50 €"]),
    ])
    _verifier(8, exercice_8, [
        ((_DEPENSES,), ["loisirs : 18.90 €", "sorties : 2.50 €", "transport : 45.00 €"]),
    ])
