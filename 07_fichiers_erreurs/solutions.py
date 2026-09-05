"""Module 07 — Solutions commentées."""

import csv


# --- Exercice 1 ---
def ecrire_lignes(chemin, lignes):
    with open(chemin, "w", encoding="utf-8") as fichier:
        for ligne in lignes:
            fichier.write(ligne + "\n")     # write n'ajoute PAS le saut de ligne
    # Le mode "w" crée le fichier s'il n'existe pas et l'écrase s'il existe.
    # Une fois sorti du bloc `with`, le fichier est refermé automatiquement,
    # même si une erreur était survenue au milieu.
    #
    # Variante plus courte, si les lignes tiennent en mémoire :
    #     fichier.write("\n".join(lignes) + "\n")


# --- Exercice 2 ---
def lire_lignes(chemin):
    lignes = []
    with open(chemin, encoding="utf-8") as fichier:
        for ligne in fichier:              # parcours ligne par ligne
            lignes.append(ligne.strip())   # ôte le \n final et les espaces
    return lignes
    # Sans strip(), on obtiendrait ["un\n", "deux\n", "trois\n"] — et toutes
    # les comparaisons ultérieures échoueraient sans qu'on voie pourquoi,
    # puisque le \n est invisible à l'écran.


# --- Exercice 3 ---
def ajouter_ligne(chemin, ligne):
    with open(chemin, "a", encoding="utf-8") as fichier:   # "a" comme append
        fichier.write(ligne + "\n")
    # Avec "w", le contenu existant serait effacé sans le moindre avertissement.
    # C'est la façon n°1 de perdre des données quand on débute.


# --- Exercice 4 ---
def lire_ou_defaut(chemin, defaut=""):
    try:
        with open(chemin, encoding="utf-8") as fichier:
            return fichier.read()
    except FileNotFoundError:
        return defaut
    # On attrape FileNotFoundError, précisément. Un `except:` nu attraperait
    # aussi une faute de frappe dans le nom d'une variable, et vous renverriez
    # le défaut en croyant que le fichier manque, alors que votre code a un bug.


# --- Exercice 5 ---
def convertir_entier(texte):
    try:
        return int(texte)
    except ValueError:
        return None
    # int("3.5") lève bien une ValueError : int() ne convertit que du texte
    # représentant un entier. Pour "3.5", il faut int(float("3.5")) — et accepter
    # que la partie décimale soit perdue.


# --- Exercice 6 ---
def diviser(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    # `if b == 0: return None` marcherait tout aussi bien ici.
    # La différence de philosophie : le if DEMANDE LA PERMISSION avant d'agir,
    # le try DEMANDE PARDON après coup. Python préfère culturellement le second,
    # surtout quand les cas d'échec sont rares : le code du cas normal reste
    # lisible, sans être criblé de vérifications préalables.


# --- Exercice 7 ---
def charger_depenses(chemin):
    try:
        with open(chemin, encoding="utf-8", newline="") as fichier:
            depenses = []
            for ligne in csv.DictReader(fichier):
                depenses.append({
                    "libelle": ligne["libelle"],
                    "montant": float(ligne["montant"]),   # le CSV rend du TEXTE
                    "categorie": ligne["categorie"],
                })
            return depenses
    except FileNotFoundError:
        return []
    # DictReader utilise la première ligne comme noms de colonnes et rend un
    # dictionnaire par ligne. On retrouve la liste de dictionnaires du module 05.
    # La conversion float() est indispensable : sans elle, "2.5" + "45.0" ferait
    # "2.545.0" au lieu de 47.5. Le CSV ne connaît que du texte.


# --- Exercice 8 ---
def sauvegarder_depenses(chemin, depenses):
    with open(chemin, "w", encoding="utf-8", newline="") as fichier:
        redacteur = csv.DictWriter(fichier, fieldnames=["libelle", "montant", "categorie"])
        redacteur.writeheader()          # sans ça, pas de ligne d'en-tête
        redacteur.writerows(depenses)
    # fieldnames fixe l'ordre des colonnes ET les clés attendues dans chaque
    # dictionnaire. Une clé en trop lève une erreur — c'est un garde-fou utile.


# --- Exercice 9 ---
def charger_depenses_tolerant(chemin):
    depenses = []
    try:
        with open(chemin, encoding="utf-8", newline="") as fichier:
            for ligne in csv.DictReader(fichier):
                try:
                    montant = float(ligne["montant"])
                except (ValueError, TypeError):
                    continue              # ligne illisible : on passe à la suivante
                depenses.append({
                    "libelle": ligne["libelle"],
                    "montant": montant,
                    "categorie": ligne["categorie"],
                })
    except FileNotFoundError:
        return []
    return depenses
    # Le try INTÉRIEUR est la clé : il entoure uniquement la conversion, à
    # l'intérieur de la boucle. S'il englobait toute la boucle, la première
    # ligne pourrie ferait perdre toutes les suivantes.
    #
    # Deux détails qui comptent :
    #   - `except (ValueError, TypeError)` — un tuple attrape plusieurs erreurs.
    #     float("") et float(None) n'échouent pas de la même façon.
    #   - `continue` saute au tour suivant sans rien ajouter (module 04).
    #
    # En vrai, on n'ignorerait pas ces lignes en silence : on les compterait
    # pour prévenir l'utilisateur (« 2 lignes ignorées »). Des données jetées
    # sans bruit, c'est un rapport faux que personne ne remarque.


if __name__ == "__main__":
    from pathlib import Path

    bac = Path(__file__).parent / "bac_a_sable"
    bac.mkdir(exist_ok=True)

    demo = bac / "demo.txt"
    ecrire_lignes(demo, ["alpha", "beta"])
    ajouter_ligne(demo, "gamma")
    print(lire_lignes(demo))
    print(lire_ou_defaut(bac / "inexistant.txt", "(défaut)"))
    print(convertir_entier("42"), convertir_entier("abc"))
    print(diviser(10, 2), diviser(5, 0))

    csv_demo = bac / "demo.csv"
    sauvegarder_depenses(csv_demo, [
        {"libelle": "Café", "montant": 2.5, "categorie": "sorties"},
    ])
    print(charger_depenses(csv_demo))
