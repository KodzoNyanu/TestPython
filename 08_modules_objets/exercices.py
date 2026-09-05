"""Module 08 — Exercices.

Lancez avec :   python exercices.py
"""

# ---------------------------------------------------------------------------
# Exercice 1 — La bibliothèque standard
# Complétez les imports nécessaires ci-dessous, puis les fonctions.
# ---------------------------------------------------------------------------
# TODO: importez ici les modules dont vous avez besoin (random, math, datetime)


def lancer_de():
    """Renvoie un entier au hasard entre 1 et 6 inclus."""
    pass  # TODO: random.randint


def hypotenuse(a, b):
    """Renvoie la longueur de l'hypoténuse d'un triangle rectangle de côtés a et b."""
    pass  # TODO: math.sqrt — a² + b² sous la racine


def date_francaise(annee, mois, jour):
    """Renvoie la date au format jj/mm/aaaa, par exemple '16/07/2026'."""
    pass  # TODO: date(annee, mois, jour).strftime("%d/%m/%Y")


# ---------------------------------------------------------------------------
# Exercice 2 — Votre première classe
# Créez une classe Livre avec :
#   - un constructeur prenant titre, auteur et pages
#   - une méthode est_long() qui renvoie True si le livre fait plus de 300 pages
#   - une méthode __repr__ qui renvoie par exemple :  Livre('1984', 'Orwell')
# ---------------------------------------------------------------------------
class Livre:
    pass  # TODO: remplacez tout le corps


# ---------------------------------------------------------------------------
# Exercice 3 — Un compte bancaire (l'état protégé)
# Créez une classe CompteBancaire avec :
#   - __init__(self, titulaire, solde=0) — refuse un solde initial négatif
#     avec `raise ValueError("Solde initial négatif")`
#   - deposer(montant) — ajoute au solde ; refuse un montant <= 0 avec
#     `raise ValueError("Montant invalide")`
#   - retirer(montant) — retire du solde ; refuse un montant <= 0 (« Montant
#     invalide ») et refuse de passer à découvert avec
#     `raise ValueError("Solde insuffisant")`
#   - solde reste accessible en tant qu'attribut : compte.solde
# L'idée : après ces méthodes, un solde négatif doit être IMPOSSIBLE.
# ---------------------------------------------------------------------------
class CompteBancaire:
    pass  # TODO


# ---------------------------------------------------------------------------
# Exercice 4 — Une classe qui contient une liste
# Créez une classe Panier avec :
#   - __init__(self) — démarre avec une liste d'articles VIDE
#     (attention : `def __init__(self, articles=[])` est le piège du module 06 !)
#   - ajouter(nom, prix) — ajoute un article (stockez ce que vous voulez :
#     un dict, un tuple...)
#   - total() — renvoie la somme des prix, 0 si le panier est vide
#   - __len__(self) — renvoie le nombre d'articles, ce qui fera marcher len(panier)
# ---------------------------------------------------------------------------
class Panier:
    pass  # TODO


# ---------------------------------------------------------------------------
# BONUS (non vérifié) — Créez un fichier `outils.py` à côté de celui-ci avec
# une fonction calculer_ttc(), et un `if __name__ == "__main__":` qui affiche
# une démo. Puis, depuis un troisième fichier, faites `import outils` et
# appelez la fonction : vérifiez que la démo ne s'affiche PAS à l'import,
# mais bien quand vous lancez outils.py directement.
# ---------------------------------------------------------------------------


# ===========================================================================
# VÉRIFICATION — ne modifiez rien en dessous.
# ===========================================================================
def _verifier(nom, condition, detail=""):
    if condition:
        print(f"OK   {nom}")
    else:
        print(f"RATE {nom}{'  -> ' + detail if detail else ''}")


def _leve(erreur_attendue, fonction, *arguments):
    """True si l'appel lève bien l'erreur attendue."""
    try:
        fonction(*arguments)
    except erreur_attendue:
        return True
    except Exception:
        return False
    return False


def _executer():
    # --- Exercice 1
    try:
        tirages = [lancer_de() for _ in range(200)]
        _verifier("exercice 1 (lancer_de)",
                  all(isinstance(t, int) and 1 <= t <= 6 for t in tirages)
                  and len(set(tirages)) > 1,
                  f"tirages obtenus : {sorted(set(tirages))}")
    except Exception as e:
        _verifier("exercice 1 (lancer_de)", False, f"a planté : {type(e).__name__} {e}")

    try:
        _verifier("exercice 1 (hypotenuse)", hypotenuse(3, 4) == 5.0,
                  f"hypotenuse(3, 4) = {hypotenuse(3, 4)!r}, attendu 5.0")
    except Exception as e:
        _verifier("exercice 1 (hypotenuse)", False, f"a planté : {type(e).__name__} {e}")

    try:
        _verifier("exercice 1 (date_francaise)", date_francaise(2026, 7, 16) == "16/07/2026",
                  f"obtenu {date_francaise(2026, 7, 16)!r}")
    except Exception as e:
        _verifier("exercice 1 (date_francaise)", False, f"a planté : {type(e).__name__} {e}")

    # --- Exercice 2
    try:
        court = Livre("Le Petit Prince", "Saint-Exupéry", 96)
        long = Livre("1984", "Orwell", 328)
        _verifier("exercice 2 (attributs)",
                  court.titre == "Le Petit Prince" and court.auteur == "Saint-Exupéry"
                  and court.pages == 96)
        _verifier("exercice 2 (est_long)", long.est_long() is True and court.est_long() is False)
        _verifier("exercice 2 (__repr__)", repr(long) == "Livre('1984', 'Orwell')",
                  f"repr obtenu : {repr(long)}")
    except Exception as e:
        _verifier("exercice 2 (Livre)", False, f"a planté : {type(e).__name__} {e}")

    # --- Exercice 3
    try:
        compte = CompteBancaire("Ada")
        _verifier("exercice 3 (solde par défaut)", compte.solde == 0)
        compte.deposer(100)
        compte.retirer(30)
        _verifier("exercice 3 (deposer/retirer)", compte.solde == 70,
                  f"solde obtenu : {compte.solde}")
        _verifier("exercice 3 (titulaire)", compte.titulaire == "Ada")
        _verifier("exercice 3 (refuse le découvert)",
                  _leve(ValueError, compte.retirer, 1000))
        _verifier("exercice 3 (solde intact après refus)", compte.solde == 70,
                  f"solde obtenu : {compte.solde} — un retrait refusé ne doit rien changer")
        _verifier("exercice 3 (refuse un dépôt négatif)",
                  _leve(ValueError, compte.deposer, -5))
        _verifier("exercice 3 (refuse un retrait négatif)",
                  _leve(ValueError, compte.retirer, -5))
        _verifier("exercice 3 (refuse un solde initial négatif)",
                  _leve(ValueError, CompteBancaire, "Bob", -10))
    except Exception as e:
        _verifier("exercice 3 (CompteBancaire)", False, f"a planté : {type(e).__name__} {e}")

    # --- Exercice 4
    try:
        panier = Panier()
        _verifier("exercice 4 (panier vide)", len(panier) == 0 and panier.total() == 0)
        panier.ajouter("Café", 2.5)
        panier.ajouter("Livre", 18.9)
        _verifier("exercice 4 (ajouter)", len(panier) == 2, f"len obtenu : {len(panier)}")
        _verifier("exercice 4 (total)", abs(panier.total() - 21.4) < 0.001,
                  f"total obtenu : {panier.total()}")
        autre = Panier()
        _verifier("exercice 4 (paniers indépendants)", len(autre) == 0,
                  f"le nouveau panier contient {len(autre)} articles — "
                  f"c'est le piège de la valeur par défaut mutable !")
    except Exception as e:
        _verifier("exercice 4 (Panier)", False, f"a planté : {type(e).__name__} {e}")


if __name__ == "__main__":
    _executer()
