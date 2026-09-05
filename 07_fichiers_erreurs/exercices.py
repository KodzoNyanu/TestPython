"""Module 07 — Exercices.

Lancez avec :   python exercices.py

Ce module manipule de VRAIS fichiers. Le vérificateur les crée dans un sous-dossier
`bac_a_sable/`, à côté de ce fichier. Vous pouvez le supprimer quand vous voulez, il
sera recréé au prochain lancement.

Rappel : toujours `with`, toujours `encoding="utf-8"`.
"""

import csv


# ---------------------------------------------------------------------------
# Exercice 1 — Écrire
# Écrivez chaque élément de `lignes` dans le fichier `chemin`, une par ligne.
# Le fichier doit être écrasé s'il existe déjà.
# N'oubliez pas le \n : write ne l'ajoute pas tout seul.
# Cette fonction ne renvoie rien.
# ---------------------------------------------------------------------------
def ecrire_lignes(chemin, lignes):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 2 — Lire
# Renvoyez la liste des lignes du fichier, SANS le saut de ligne final.
#     un fichier contenant "a\nb\nc\n"  ->  ["a", "b", "c"]
# Parcourez le fichier ligne par ligne et pensez à strip().
# ---------------------------------------------------------------------------
def lire_lignes(chemin):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 3 — Ajouter sans écraser
# Ajoutez `ligne` à la FIN du fichier, sans toucher à ce qu'il contient déjà.
# Si vous voyez le contenu précédent disparaître, vous avez utilisé le mauvais mode.
# ---------------------------------------------------------------------------
def ajouter_ligne(chemin, ligne):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 4 — Le fichier absent
# Renvoyez le contenu du fichier (la chaîne complète, telle quelle).
# Si le fichier n'existe pas, renvoyez `defaut` au lieu de planter.
# Attrapez l'erreur PRÉCISE, pas un except nu.
# ---------------------------------------------------------------------------
def lire_ou_defaut(chemin, defaut=""):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 5 — La conversion prudente
# Renvoyez le texte converti en entier, ou None si ce n'est pas convertible.
#     "42" -> 42        "abc" -> None       "" -> None      "3.5" -> None
# (Oui, "3.5" échoue : int() n'accepte pas de texte à virgule. Testez-le.)
# ---------------------------------------------------------------------------
def convertir_entier(texte):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 6 — La division prudente
# Renvoyez a / b, ou None si b vaut 0.
# Faites-le avec try/except plutôt qu'avec un if : ici les deux se valent, mais
# c'est l'occasion d'écrire le bloc. (Le débat « demander la permission ou
# demander pardon » est un classique ; en Python, la culture penche pour try.)
# ---------------------------------------------------------------------------
def diviser(a, b):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 7 — Charger un CSV
# Le fichier a les colonnes : libelle,montant,categorie
# Renvoyez une liste de dictionnaires, en convertissant montant en float :
#     [{"libelle": "Café", "montant": 2.5, "categorie": "sorties"}, ...]
# Si le fichier n'existe pas, renvoyez une liste vide.
# Utilisez csv.DictReader, et n'oubliez pas newline="".
# ---------------------------------------------------------------------------
def charger_depenses(chemin):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 8 — Sauvegarder un CSV
# Écrivez la liste de dictionnaires dans le fichier, avec la ligne d'en-tête
# libelle,montant,categorie. Ne renvoie rien.
# Utilisez csv.DictWriter (writeheader puis writerows).
# ---------------------------------------------------------------------------
def sauvegarder_depenses(chemin, depenses):
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 9 — La ligne corrompue
# Même chose que l'exercice 7, mais le fichier vient du monde réel : certaines
# lignes ont un montant illisible ("douze", "", "N/A"...).
# IGNOREZ ces lignes et renvoyez les autres. Une seule ligne pourrie ne doit
# pas faire échouer tout le chargement.
# C'est exactement le genre de code que vous écrirez en data, tous les jours.
# ---------------------------------------------------------------------------
def charger_depenses_tolerant(chemin):
    pass  # TODO


# ---------------------------------------------------------------------------
# BONUS (non vérifié) — Écrivez demander_entier(question) : elle redemande
# jusqu'à obtenir un entier valide (while True + try + return). Testez-la dans
# un fichier à part en tapant n'importe quoi : elle ne doit jamais planter.
# ---------------------------------------------------------------------------


# ===========================================================================
# VÉRIFICATION — ne modifiez rien en dessous.
# ===========================================================================
from pathlib import Path

_BAC = Path(__file__).parent / "bac_a_sable"


def _verifier(nom, condition, detail=""):
    if condition:
        print(f"OK   {nom}")
    else:
        print(f"RATE {nom}{'  -> ' + detail if detail else ''}")


def _lire_brut(chemin):
    try:
        return Path(chemin).read_text(encoding="utf-8")
    except FileNotFoundError:
        return None


def _executer():
    _BAC.mkdir(exist_ok=True)
    for ancien in _BAC.glob("*"):
        ancien.unlink()

    # --- Exercice 1
    f1 = _BAC / "ex1.txt"
    try:
        ecrire_lignes(f1, ["alpha", "beta", "gamma"])
        _verifier("exercice 1 (ecrire_lignes)", _lire_brut(f1) == "alpha\nbeta\ngamma\n",
                  f"contenu obtenu : {_lire_brut(f1)!r}")
    except Exception as e:
        _verifier("exercice 1 (ecrire_lignes)", False, f"a planté : {type(e).__name__} {e}")

    # --- Exercice 2
    f2 = _BAC / "ex2.txt"
    f2.write_text("un\ndeux\ntrois\n", encoding="utf-8")
    try:
        _verifier("exercice 2 (lire_lignes)", lire_lignes(f2) == ["un", "deux", "trois"],
                  f"obtenu : {lire_lignes(f2)!r}")
    except Exception as e:
        _verifier("exercice 2 (lire_lignes)", False, f"a planté : {type(e).__name__} {e}")

    # --- Exercice 3
    f3 = _BAC / "ex3.txt"
    f3.write_text("existant\n", encoding="utf-8")
    try:
        ajouter_ligne(f3, "nouveau")
        _verifier("exercice 3 (ajouter_ligne)", _lire_brut(f3) == "existant\nnouveau\n",
                  f"contenu obtenu : {_lire_brut(f3)!r} (le mode w écrase, le mode a ajoute)")
    except Exception as e:
        _verifier("exercice 3 (ajouter_ligne)", False, f"a planté : {type(e).__name__} {e}")

    # --- Exercice 4
    f4 = _BAC / "ex4.txt"
    f4.write_text("coucou", encoding="utf-8")
    try:
        ok = (lire_ou_defaut(f4) == "coucou"
              and lire_ou_defaut(_BAC / "jamais.txt", "rien") == "rien"
              and lire_ou_defaut(_BAC / "jamais.txt") == "")
        _verifier("exercice 4 (lire_ou_defaut)", ok)
    except Exception as e:
        _verifier("exercice 4 (lire_ou_defaut)", False, f"a planté : {type(e).__name__} {e}")

    # --- Exercice 5
    cas5 = [("42", 42), ("-7", -7), ("abc", None), ("", None), ("3.5", None)]
    echecs = [f"{t!r} -> {convertir_entier(t)!r} (attendu {a!r})"
              for t, a in cas5 if convertir_entier(t) != a]
    _verifier("exercice 5 (convertir_entier)", not echecs, " ; ".join(echecs))

    # --- Exercice 6
    cas6 = [((10, 2), 5.0), ((7, 2), 3.5), ((5, 0), None), ((0, 5), 0.0)]
    echecs = [f"{a} -> {diviser(*a)!r} (attendu {r!r})" for a, r in cas6 if diviser(*a) != r]
    _verifier("exercice 6 (diviser)", not echecs, " ; ".join(echecs))

    # --- Exercices 7 et 8
    f7 = _BAC / "depenses.csv"
    f7.write_text(
        "libelle,montant,categorie\n"
        "Café,2.5,sorties\n"
        "Train,45.0,transport\n",
        encoding="utf-8", newline="",
    )
    attendu7 = [
        {"libelle": "Café", "montant": 2.5, "categorie": "sorties"},
        {"libelle": "Train", "montant": 45.0, "categorie": "transport"},
    ]
    try:
        obtenu7 = charger_depenses(f7)
        _verifier("exercice 7 (charger_depenses)", obtenu7 == attendu7, f"obtenu : {obtenu7!r}")
        _verifier("exercice 7 (fichier absent)", charger_depenses(_BAC / "vide.csv") == [])
    except Exception as e:
        _verifier("exercice 7 (charger_depenses)", False, f"a planté : {type(e).__name__} {e}")

    f8 = _BAC / "sortie.csv"
    try:
        sauvegarder_depenses(f8, attendu7)
        relu = charger_depenses(f8)
        _verifier("exercice 8 (sauvegarder_depenses)", relu == attendu7,
                  f"relu : {relu!r} — contenu : {_lire_brut(f8)!r}")
    except Exception as e:
        _verifier("exercice 8 (sauvegarder_depenses)", False, f"a planté : {type(e).__name__} {e}")

    # --- Exercice 9
    f9 = _BAC / "sale.csv"
    f9.write_text(
        "libelle,montant,categorie\n"
        "Café,2.5,sorties\n"
        "Mystère,douze,divers\n"
        "Train,45.0,transport\n"
        "Trou,,divers\n"
        "Livre,18.9,loisirs\n",
        encoding="utf-8", newline="",
    )
    attendu9 = [
        {"libelle": "Café", "montant": 2.5, "categorie": "sorties"},
        {"libelle": "Train", "montant": 45.0, "categorie": "transport"},
        {"libelle": "Livre", "montant": 18.9, "categorie": "loisirs"},
    ]
    try:
        obtenu9 = charger_depenses_tolerant(f9)
        _verifier("exercice 9 (charger_depenses_tolerant)", obtenu9 == attendu9,
                  f"obtenu : {obtenu9!r}")
    except Exception as e:
        _verifier("exercice 9 (charger_depenses_tolerant)", False,
                  f"a planté : {type(e).__name__} {e}")


if __name__ == "__main__":
    _executer()
