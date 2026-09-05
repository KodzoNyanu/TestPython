"""Projet final — Solution complète et commentée.

À consulter APRÈS avoir sérieusement bataillé avec gestionnaire.py. La valeur de
ce projet est dans les heures que vous passez à le faire marcher, pas dans la
lecture de cette page.

Pour l'essayer :   python solution_gestionnaire.py
Pour les tests :   python solution_gestionnaire.py --test
"""

import csv
from pathlib import Path

FICHIER = Path(__file__).parent / "mes_depenses.csv"
COLONNES = ["libelle", "montant", "categorie"]

# Les constantes en majuscules, en haut du fichier : quand le nom du fichier
# change, on le corrige à un seul endroit. Une valeur écrite en dur au milieu
# du code est une valeur qu'on oubliera de changer quelque part.


# ===========================================================================
# ÉTAPE 1 — La classe Depense
# ===========================================================================
class Depense:
    """Une dépense : un libellé, un montant en euros, une catégorie."""

    def __init__(self, libelle, montant, categorie="divers"):
        montant = float(montant)          # accepte 2.5 comme "2.5" (le CSV rend du texte)
        if not libelle:
            raise ValueError("Le libellé ne peut pas être vide")
        if montant < 0:
            raise ValueError("Le montant ne peut pas être négatif")
        self.libelle = libelle
        self.montant = montant
        self.categorie = categorie

    def __repr__(self):
        return f"Depense({self.libelle!r}, {self.montant}, {self.categorie!r})"

    # La conversion vient AVANT les tests : comparer une chaîne à 0 lèverait un
    # TypeError. Au passage, float("douze") lève une ValueError — exactement
    # l'erreur que charger() attrape pour ignorer les lignes pourries. Le
    # constructeur fait donc d'une pierre deux coups : il valide ET il rejette
    # les données illisibles, avec le même mécanisme.


# ===========================================================================
# ÉTAPE 2 — Le stockage
# ===========================================================================
def charger(chemin):
    """Renvoie la liste des Depense lues dans le fichier CSV."""
    depenses = []
    try:
        with open(chemin, encoding="utf-8", newline="") as fichier:
            for ligne in csv.DictReader(fichier):
                try:
                    depenses.append(Depense(
                        ligne["libelle"],
                        ligne["montant"],
                        ligne["categorie"],
                    ))
                except (ValueError, KeyError):
                    continue          # ligne inexploitable : on l'ignore
    except FileNotFoundError:
        return []                     # premier lancement : c'est normal
    return depenses
    # Deux try imbriqués, deux rôles bien distincts :
    #   - l'extérieur gère l'absence du fichier (une fois, au début) ;
    #   - l'intérieur gère une ligne fautive (à chaque tour), pour que la
    #     ligne 3 ne fasse pas perdre les lignes 4 à 100.
    # KeyError est attrapée aussi : un CSV sans la colonne "categorie" échouerait
    # là plutôt qu'avec une ValueError.


def sauvegarder(chemin, depenses):
    """Écrit les dépenses dans le fichier CSV."""
    with open(chemin, "w", encoding="utf-8", newline="") as fichier:
        redacteur = csv.DictWriter(fichier, fieldnames=COLONNES)
        redacteur.writeheader()
        for depense in depenses:
            redacteur.writerow({
                "libelle": depense.libelle,
                "montant": depense.montant,
                "categorie": depense.categorie,
            })
    # Un objet n'est pas un dictionnaire : DictWriter attend des dicts, il faut
    # donc traduire. (Il existe des outils pour automatiser ça — dataclasses,
    # __dict__ — mais l'explicite reste très bien ici.)


# ===========================================================================
# ÉTAPE 3 — Les calculs
# ===========================================================================
def total(depenses):
    """Renvoie la somme des montants (0 si la liste est vide)."""
    return sum(depense.montant for depense in depenses)
    # sum([]) vaut 0 : le cas vide se traite tout seul, pas besoin de if.


def moyenne(depenses):
    """Renvoie le montant moyen, ou None si la liste est vide."""
    if not depenses:
        return None               # sinon : ZeroDivisionError
    return total(depenses) / len(depenses)
    # On réutilise total() au lieu de refaire la somme. Une seule définition
    # de « le total », donc une seule chose à corriger le jour où elle change.


def total_par_categorie(depenses):
    """Renvoie un dict {categorie: total}."""
    totaux = {}
    for depense in depenses:
        totaux[depense.categorie] = totaux.get(depense.categorie, 0) + depense.montant
    return totaux
    # Le group by du module 05, à l'identique. Sur un objet on écrit
    # depense.categorie plutôt que depense["categorie"] — c'est la seule différence.


def plus_grosse(depenses):
    """Renvoie la Depense au montant le plus élevé, ou None si la liste est vide."""
    if not depenses:
        return None
    return max(depenses, key=lambda depense: depense.montant)
    # `key` dit à max SUR QUOI comparer : sans lui, Python ne saurait pas
    # comparer deux Depense entre elles et lèverait un TypeError.
    # `lambda depense: depense.montant` est une mini-fonction anonyme, l'équivalent
    # de :  def extraire(depense): return depense.montant
    #
    # La version manuelle, si lambda vous gêne encore :
    #     championne = depenses[0]
    #     for depense in depenses[1:]:
    #         if depense.montant > championne.montant:
    #             championne = depense
    #     return championne


# ===========================================================================
# ÉTAPE 4 — L'affichage
# ===========================================================================
def afficher_liste(depenses):
    """Affiche les dépenses numérotées à partir de 1."""
    if not depenses:
        print("\nAucune dépense enregistrée.")
        return                    # on sort tôt : le reste ne concerne que le cas non vide

    print("\n--- Mes dépenses ---")
    for numero, depense in enumerate(depenses, start=1):
        print(f"{numero:2}. {depense.libelle:<25} {depense.montant:>8.2f} €  [{depense.categorie}]")
    print(f"    {'TOTAL':<25} {total(depenses):>8.2f} €")
    # Les formats font l'alignement :
    #   :<25   texte calé à gauche sur 25 caractères
    #   :>8.2f nombre calé à droite sur 8 caractères, 2 décimales
    # C'est ce qui aligne les colonnes au lieu d'un magma illisible.


def afficher_statistiques(depenses):
    """Affiche les statistiques avec un histogramme en barres."""
    if not depenses:
        print("\nAucune dépense : rien à analyser.")
        return

    somme = total(depenses)
    grosse = plus_grosse(depenses)

    print("\n--- Statistiques ---")
    print(f"Total           : {somme:.2f} €")
    print(f"Nombre          : {len(depenses)}")
    print(f"Dépense moyenne : {moyenne(depenses):.2f} €")
    print(f"Plus grosse     : {grosse.libelle} ({grosse.montant:.2f} €)")

    print("\nPar catégorie :")
    totaux = total_par_categorie(depenses)
    for categorie, montant in sorted(totaux.items(), key=lambda paire: -paire[1]):
        part = montant / somme                    # entre 0 et 1
        barre = "#" * int(part * 20)              # 20 caractères pour 100 %
        print(f"  {categorie:<14} {montant:>8.2f} €  {barre:<20} {part:>5.1%}")

    # sorted(..., key=lambda paire: -paire[1]) : on trie les couples
    # (categorie, montant) sur le montant, en négatif pour obtenir l'ordre
    # décroissant. Équivalent plus lisible : sorted(..., key=..., reverse=True).
    #
    # Le format :.1% multiplie par 100 et ajoute le signe % : 0.678 -> 67.8%.
    #
    # POURQUOI DES # ET PAS DE BEAUX BLOCS █ ? Parce que la console Windows écrit
    # en cp1252, un jeu de caractères qui ignore tout ce qui sort du latin. Un
    # print("█") y lève un UnicodeEncodeError et TUE le programme — alors que le
    # même code marche parfaitement sous Linux ou dans VS Code. Les accents, eux,
    # passent : ils font partie de cp1252.
    # Si vous y tenez, `python -X utf8 votre_fichier.py` force l'UTF-8, et la
    # variable d'environnement PYTHONUTF8=1 le fait pour de bon. Mais un
    # programme qui ne dépend pas de la configuration du poste est plus solide
    # qu'un programme qui exige la bonne. C'est un arbitrage qu'on refait souvent :
    # le joli qui casse ailleurs, ou le simple qui marche partout.
    #
    # Toutes ces fonctions d'affichage ne calculent RIEN : elles appellent les
    # fonctions de l'étape 3. C'est la raison pour laquelle on peut tester les
    # calculs automatiquement, et pour laquelle passer à une sortie HTML ne
    # demanderait de réécrire que cette section.


# ===========================================================================
# ÉTAPE 5 — Le menu
# ===========================================================================
def demander_texte(question):
    """Redemande tant que la saisie est vide."""
    while True:
        reponse = input(question).strip()
        if reponse:
            return reponse
        print("  Une réponse est attendue.")


def demander_montant(question):
    """Redemande tant que la saisie n'est pas un nombre positif valide."""
    while True:
        saisie = input(question).strip().replace(",", ".")   # « 2,50 » -> « 2.50 »
        try:
            montant = float(saisie)
        except ValueError:
            print("  Ce n'est pas un nombre. Exemple : 12.50")
            continue
        if montant < 0:
            print("  Le montant ne peut pas être négatif.")
            continue
        return montant
    # while True + return : la seule sortie est une saisie valide. L'utilisateur
    # peut taper « douze », « », « -3 » ou son prénom, le programme tient bon.
    # C'est un investissement de dix lignes qui évite tous les plantages du monde
    # réel — et le monde réel commence par taper n'importe quoi.


def ajouter_depense(depenses):
    """Demande les informations et ajoute la dépense à la liste."""
    print("\n--- Nouvelle dépense ---")
    libelle = demander_texte("Libellé      : ")
    montant = demander_montant("Montant en € : ")
    categorie = input("Catégorie (défaut : divers) : ").strip() or "divers"
    # `x or "divers"` renvoie x s'il est « vrai », sinon "divers".
    # C'est une écriture idiomatique pour « valeur, ou défaut si vide ».

    depenses.append(Depense(libelle, montant, categorie))
    print(f"Ajouté : {libelle} ({montant:.2f} €)")


def supprimer_depense(depenses):
    """Affiche la liste, demande un numéro, supprime la dépense correspondante."""
    if not depenses:
        print("\nRien à supprimer.")
        return

    afficher_liste(depenses)
    try:
        numero = int(input("\nNuméro à supprimer (0 pour annuler) : "))
    except ValueError:
        print("Numéro invalide.")
        return

    if numero == 0:
        return
    if not 1 <= numero <= len(depenses):
        print(f"Il n'y a pas de dépense n°{numero}.")
        return

    supprimee = depenses.pop(numero - 1)     # -1 : l'humain compte à partir de 1
    print(f"Supprimé : {supprimee.libelle}")
    # Le décalage entre les numéros affichés (1, 2, 3...) et les indices de la
    # liste (0, 1, 2...) est une source de bugs éternelle. On le traite à un seul
    # endroit, ici, au moment précis où l'on passe du monde humain au monde machine.


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
    print(f"{len(depenses)} dépense(s) chargée(s) depuis {FICHIER.name}")

    while True:
        afficher_menu()
        choix = input("\nVotre choix : ").strip()

        if choix == "1":
            ajouter_depense(depenses)
            sauvegarder(FICHIER, depenses)
        elif choix == "2":
            afficher_liste(depenses)
        elif choix == "3":
            afficher_statistiques(depenses)
        elif choix == "4":
            supprimer_depense(depenses)
            sauvegarder(FICHIER, depenses)
        elif choix == "5":
            sauvegarder(FICHIER, depenses)
            print("Données enregistrées. À bientôt !")
            break
        else:
            print("Choix invalide : tapez un chiffre entre 1 et 5.")

    # On sauvegarde après chaque modification, pas seulement en quittant : si le
    # programme est fermé brutalement (Ctrl+C, coupure), le travail est déjà sur
    # le disque. Écrire un CSV de 50 lignes ne coûte rien ; refaire la saisie de
    # l'utilisateur, si.
    #
    # Regardez la taille de principal() : quinze lignes, qui se lisent comme le
    # menu lui-même. Tout le travail est ailleurs, dans des fonctions nommées.
    # C'est ça, un programme bien découpé — et c'est la seule raison pour laquelle
    # 250 lignes restent compréhensibles.


# ===========================================================================
# TESTS
# ===========================================================================
def _verifier(nom, condition, detail=""):
    print(f"OK   {nom}" if condition else f"RATE {nom}{'  -> ' + detail if detail else ''}")


def _tests():
    import tempfile

    dossier = Path(tempfile.mkdtemp())
    jeu = [
        Depense("Café", 2.5, "sorties"),
        Depense("Train", 45.0, "transport"),
        Depense("Livre", 18.9, "loisirs"),
        Depense("Métro", 16.9, "transport"),
    ]

    _verifier("repr", repr(jeu[0]) == "Depense('Café', 2.5, 'sorties')")
    _verifier("total", abs(total(jeu) - 83.3) < 0.001)
    _verifier("total vide", total([]) == 0)
    _verifier("moyenne", abs(moyenne(jeu) - 20.825) < 0.001)
    _verifier("moyenne vide", moyenne([]) is None)
    _verifier("par catégorie", total_par_categorie(jeu)["transport"] == 61.9)
    _verifier("plus grosse", plus_grosse(jeu).libelle == "Train")
    _verifier("plus grosse vide", plus_grosse([]) is None)

    cible = dossier / "t.csv"
    sauvegarder(cible, jeu)
    _verifier("aller-retour disque", len(charger(cible)) == 4)
    _verifier("fichier absent", charger(dossier / "nope.csv") == [])

    sale = dossier / "sale.csv"
    sale.write_text("libelle,montant,categorie\nA,1.0,x\nB,douze,y\nC,3.0,z\n",
                    encoding="utf-8", newline="")
    _verifier("ligne pourrie ignorée", len(charger(sale)) == 2)

    for mauvais in [("", 2.5), ("X", -5)]:
        try:
            Depense(*mauvais)
            _verifier(f"refuse {mauvais}", False)
        except ValueError:
            _verifier(f"refuse {mauvais}", True)

    print("\n--- Démo de l'affichage ---")
    afficher_liste(jeu)
    afficher_statistiques(jeu)


if __name__ == "__main__":
    import sys

    if "--test" in sys.argv:
        _tests()
    else:
        principal()
