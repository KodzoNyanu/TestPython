"""Projet final — Gestionnaire de dépenses.

Squelette à compléter. Lisez cahier_des_charges.md d'abord.

DEUX FAÇONS DE LANCER CE FICHIER :

    python gestionnaire.py --test     lance les tests automatiques des étapes 1 à 3
    python gestionnaire.py            lance le programme (menu interactif)

Travaillez étape par étape : complétez l'étape 1, lancez --test, corrigez, et
seulement ensuite passez à l'étape 2. Un programme qui marche à chaque instant,
c'est un programme dont vous savez toujours où est le bug : dans ce que vous
venez d'écrire.
"""

import csv
from pathlib import Path

FICHIER = Path(__file__).parent / "mes_depenses.csv"
COLONNES = ["libelle", "montant", "categorie"]


# ===========================================================================
# ÉTAPE 1 — La classe Depense
# ===========================================================================
class Depense:
    """Une dépense : un libellé, un montant en euros, une catégorie.

    Le constructeur refuse un libellé vide ou un montant négatif : une fois
    l'objet créé, on est certain qu'il est valide.
    """

    def __init__(self, libelle, montant, categorie="divers"):
        # TODO: validez (raise ValueError) puis rangez dans self.
        # - libelle vide            -> ValueError("Le libellé ne peut pas être vide")
        # - montant strictement < 0 -> ValueError("Le montant ne peut pas être négatif")
        # Pensez à convertir le montant en float : il arrivera parfois en texte.
        pass  # TODO

    def __repr__(self):
        # TODO: renvoyez par exemple  Depense('Café', 2.5, 'sorties')
        pass  # TODO


# ===========================================================================
# ÉTAPE 2 — Le stockage
# ===========================================================================
def charger(chemin):
    """Renvoie la liste des Depense lues dans le fichier CSV.

    Fichier absent -> liste vide. Ligne illisible -> ignorée en silence.
    """
    # TODO:
    #  - ouvrir avec encoding="utf-8" et newline=""
    #  - csv.DictReader
    #  - pour chaque ligne, essayer de construire une Depense ; en cas de
    #    ValueError, passer à la suivante (continue)
    #  - FileNotFoundError -> return []
    pass  # TODO


def sauvegarder(chemin, depenses):
    """Écrit les dépenses dans le fichier CSV, en écrasant le contenu précédent."""
    # TODO: csv.DictWriter avec fieldnames=COLONNES, writeheader(), puis une
    # writerow par dépense. Un objet Depense n'est PAS un dictionnaire : il faut
    # construire {"libelle": d.libelle, ...} pour chacun.
    pass  # TODO


# ===========================================================================
# ÉTAPE 3 — Les calculs  (aucun print ici ! ces fonctions RENVOIENT)
# ===========================================================================
def total(depenses):
    """Renvoie la somme des montants (0 si la liste est vide)."""
    pass  # TODO


def moyenne(depenses):
    """Renvoie le montant moyen, ou None si la liste est vide."""
    pass  # TODO


def total_par_categorie(depenses):
    """Renvoie un dict {categorie: total}. C'est le « group by » du module 05."""
    pass  # TODO


def plus_grosse(depenses):
    """Renvoie la Depense au montant le plus élevé, ou None si la liste est vide."""
    # Indice : max(depenses, key=...) sait le faire, mais une boucle avec un
    # champion provisoire marche tout aussi bien. Faites au plus clair pour vous.
    pass  # TODO


# ===========================================================================
# ÉTAPE 4 — L'affichage  (ici, et SEULEMENT ici, on a le droit de print)
# ===========================================================================
def afficher_liste(depenses):
    """Affiche les dépenses numérotées à partir de 1.

    Format suggéré :   1. Café                    2.50 €  [sorties]
    Si la liste est vide, le dire.
    """
    pass  # TODO


def afficher_statistiques(depenses):
    """Affiche le total, le nombre, la moyenne, la plus grosse, et le détail
    par catégorie avec une barre proportionnelle et un pourcentage.

    Indice pour la barre : "#" * int(part * 20) où part est la proportion (0 à 1).
    (Tenté par un joli bloc plein "█" ? La console Windows écrit en cp1252 et
     lève un UnicodeEncodeError dessus — votre programme meurt sur un caractère
     décoratif. Restez en ASCII pour ce qui va à l'écran.)
    Trier les catégories du plus gros total au plus petit :
        for categorie, montant in sorted(totaux.items(), key=lambda x: -x[1]):
    (le `key=lambda x: -x[1]` veut dire « trie sur la 2e valeur, à l'envers » ;
     lambda est une mini-fonction anonyme, voir le module 10)
    """
    pass  # TODO


# ===========================================================================
# ÉTAPE 5 — Le menu
# ===========================================================================
def demander_texte(question):
    """Redemande tant que la saisie est vide. Renvoie le texte saisi."""
    pass  # TODO


def demander_montant(question):
    """Redemande tant que la saisie n'est pas un nombre positif valide.

    Acceptez la virgule française : "2,50" doit marcher aussi bien que "2.50".
    Indice : texte.replace(",", ".") avant la conversion.
    """
    pass  # TODO


def ajouter_depense(depenses):
    """Demande les informations à l'utilisateur et ajoute la dépense à la liste."""
    pass  # TODO


def supprimer_depense(depenses):
    """Affiche la liste, demande un numéro, supprime la dépense correspondante.

    Attention : l'utilisateur voit des numéros à partir de 1, la liste s'indexe
    à partir de 0. Un numéro hors limites ne doit pas planter le programme.
    """
    pass  # TODO


def afficher_menu():
    print("\n=== MES DÉPENSES ===")
    print("1. Ajouter une dépense")
    print("2. Lister les dépenses")
    print("3. Statistiques")
    print("4. Supprimer une dépense")
    print("5. Quitter")


def principal():
    """Boucle principale du programme."""
    depenses = charger(FICHIER)
    print(f"{len(depenses)} dépense(s) chargée(s).")

    # TODO: la boucle while : afficher le menu, lire le choix, agir, recommencer.
    # Sauvegardez après chaque modification — un plantage ne doit pas coûter
    # les données de l'utilisateur.
    pass  # TODO


# ===========================================================================
# TESTS AUTOMATIQUES DES ÉTAPES 1 À 3 — ne modifiez rien en dessous.
# Lancez avec :   python gestionnaire.py --test
# ===========================================================================
def _verifier(nom, condition, detail=""):
    if condition:
        print(f"OK   {nom}")
    else:
        print(f"RATE {nom}{'  -> ' + detail if detail else ''}")


def _tests():
    import sys
    import tempfile

    print("--- Étape 1 : la classe Depense ---")
    try:
        cafe = Depense("Café", 2.5, "sorties")
        _verifier("attributs", cafe.libelle == "Café" and cafe.montant == 2.5
                  and cafe.categorie == "sorties")
        _verifier("montant converti en float", isinstance(Depense("X", "2.5").montant, float),
                  "Depense('X', '2.5').montant doit valoir 2.5, pas '2.5'")
        _verifier("catégorie par défaut", Depense("X", 1).categorie == "divers")
        _verifier("__repr__", repr(cafe) == "Depense('Café', 2.5, 'sorties')",
                  f"obtenu : {repr(cafe)}")
        for mauvais, quoi in [(("", 2.5), "libellé vide"), (("X", -5), "montant négatif")]:
            try:
                Depense(*mauvais)
                _verifier(f"refuse un {quoi}", False, "aucune erreur levée")
            except ValueError:
                _verifier(f"refuse un {quoi}", True)
            except Exception as e:
                _verifier(f"refuse un {quoi}", False, f"mauvaise erreur : {type(e).__name__}")
    except Exception as e:
        _verifier("étape 1", False, f"a planté : {type(e).__name__} {e}")
        return

    print("\n--- Étape 2 : le stockage ---")
    try:
        dossier = Path(tempfile.mkdtemp())
        temoins = [Depense("Café", 2.5, "sorties"), Depense("Train", 45.0, "transport")]
        cible = dossier / "test.csv"
        sauvegarder(cible, temoins)
        relu = charger(cible)
        _verifier("aller-retour disque",
                  relu is not None and len(relu) == 2
                  and relu[0].libelle == "Café" and relu[0].montant == 2.5
                  and relu[1].categorie == "transport",
                  f"relu : {relu!r}")
        _verifier("fichier absent -> liste vide", charger(dossier / "nope.csv") == [])
        sale = dossier / "sale.csv"
        sale.write_text("libelle,montant,categorie\nA,1.0,x\nB,douze,y\nC,3.0,z\n",
                        encoding="utf-8", newline="")
        propre = charger(sale)
        _verifier("ligne illisible ignorée, le reste passe",
                  propre is not None and len(propre) == 2,
                  f"obtenu {len(propre) if propre is not None else None} dépense(s), attendu 2")
    except Exception as e:
        _verifier("étape 2", False, f"a planté : {type(e).__name__} {e}")

    print("\n--- Étape 3 : les calculs ---")
    jeu = [
        Depense("Café", 2.5, "sorties"),
        Depense("Train", 45.0, "transport"),
        Depense("Livre", 18.9, "loisirs"),
        Depense("Métro", 16.9, "transport"),
    ]
    try:
        _verifier("total", abs(total(jeu) - 83.3) < 0.001, f"obtenu {total(jeu)!r}")
        _verifier("total d'une liste vide", total([]) == 0, f"obtenu {total([])!r}")
        _verifier("moyenne", abs(moyenne(jeu) - 20.825) < 0.001, f"obtenu {moyenne(jeu)!r}")
        _verifier("moyenne d'une liste vide", moyenne([]) is None, f"obtenu {moyenne([])!r}")
        attendu = {"sorties": 2.5, "transport": 61.9, "loisirs": 18.9}
        obtenu = total_par_categorie(jeu)
        _verifier("total par catégorie",
                  obtenu is not None and set(obtenu) == set(attendu)
                  and all(abs(obtenu[c] - attendu[c]) < 0.001 for c in attendu),
                  f"obtenu {obtenu!r}")
        _verifier("total par catégorie d'une liste vide", total_par_categorie([]) == {})
        grosse = plus_grosse(jeu)
        _verifier("plus grosse", grosse is not None and grosse.libelle == "Train",
                  f"obtenu {grosse!r}")
        _verifier("plus grosse d'une liste vide", plus_grosse([]) is None)
    except Exception as e:
        _verifier("étape 3", False, f"a planté : {type(e).__name__} {e}")

    print("\nLes étapes 4 et 5 se testent à la main : lancez `python gestionnaire.py`,")
    print("et tapez n'importe quoi pour essayer de le faire planter.")


if __name__ == "__main__":
    import sys

    if "--test" in sys.argv:
        _tests()
    else:
        principal()
