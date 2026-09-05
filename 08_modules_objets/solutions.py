"""Module 08 — Solutions commentées."""

import math
import random
from datetime import date


# --- Exercice 1 ---
def lancer_de():
    """Renvoie un entier au hasard entre 1 et 6 inclus."""
    return random.randint(1, 6)
    # Attention : randint inclut LES DEUX bornes, contrairement à range(1, 6)
    # qui s'arrête à 5. C'est une exception à la règle habituelle — le genre de
    # détail qu'on vérifie dans la documentation plutôt que de le deviner.


def hypotenuse(a, b):
    """Renvoie la longueur de l'hypoténuse d'un triangle rectangle de côtés a et b."""
    return math.sqrt(a ** 2 + b ** 2)
    # math.hypot(a, b) fait exactement ça, en mieux (plus précis sur les
    # valeurs extrêmes). Toujours le même réflexe : chercher avant d'écrire.


def date_francaise(annee, mois, jour):
    """Renvoie la date au format jj/mm/aaaa."""
    return date(annee, mois, jour).strftime("%d/%m/%Y")
    # strftime formate une date selon un motif : %d le jour, %m le mois,
    # %Y l'année sur 4 chiffres. Inutile d'apprendre la liste par cœur.


# --- Exercice 2 ---
class Livre:
    """Un livre, décrit par son titre, son auteur et son nombre de pages."""

    def __init__(self, titre, auteur, pages):
        self.titre = titre       # self.titre (durable) reçoit titre (le paramètre)
        self.auteur = auteur
        self.pages = pages

    def est_long(self):
        return self.pages > 300      # une comparaison EST déjà un booléen

    def __repr__(self):
        return f"Livre({self.titre!r}, {self.auteur!r})"
        # Le !r applique repr() à la valeur, ce qui remet les guillemets autour
        # du texte : on obtient Livre('1984', 'Orwell') et non Livre(1984, Orwell).
        # La convention pour __repr__ est de ressembler au code qui recréerait l'objet.


# --- Exercice 3 ---
class CompteBancaire:
    """Un compte bancaire dont le solde ne peut jamais devenir négatif."""

    def __init__(self, titulaire, solde=0):
        if solde < 0:
            raise ValueError("Solde initial négatif")
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Montant invalide")
        self.solde += montant

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Montant invalide")
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant

    # Tout l'intérêt est là : les contrôles sont DANS la classe, à un seul
    # endroit, et on ne peut pas les contourner. Avec un simple dictionnaire,
    # il aurait fallu penser à vérifier avant chaque opération, partout dans le
    # programme — et il aurait suffi d'un oubli pour créer un solde négatif.
    #
    # Remarquez aussi l'ordre dans retirer() : on vérifie AVANT de modifier.
    # Une opération refusée doit laisser l'objet exactement comme elle l'a trouvé ;
    # un objet à moitié modifié est bien pire qu'une opération qui échoue.
    #
    # Pourquoi raise plutôt que `return False` ? Parce qu'un appelant peut ignorer
    # une valeur de retour sans le vouloir, alors qu'une erreur, il faut la traiter :
    #     try:
    #         compte.retirer(1000)
    #     except ValueError as erreur:
    #         print(f"Opération refusée : {erreur}")


# --- Exercice 4 ---
class Panier:
    """Un panier d'achats."""

    def __init__(self):
        self.articles = []       # une liste NEUVE pour chaque panier
        # Le piège évité : `def __init__(self, articles=[])`. Cette liste-là
        # serait créée UNE SEULE FOIS, à la définition de la classe, et partagée
        # par tous les paniers : ajouter un café au panier d'Ada le ferait
        # apparaître dans celui de Bob. Ici, self.articles = [] s'exécute à
        # chaque construction, donc chaque objet a bien la sienne.

    def ajouter(self, nom, prix):
        self.articles.append({"nom": nom, "prix": prix})

    def total(self):
        return sum(article["prix"] for article in self.articles)
        # sum() sur une liste vide renvoie 0 : le cas du panier vide est déjà
        # traité, sans avoir besoin d'un if.

    def __len__(self):
        return len(self.articles)
        # Définir __len__ fait marcher len(panier). C'est le principe des méthodes
        # magiques : on branche son objet sur la syntaxe du langage, et il se
        # comporte comme un type natif. On aurait pu ajouter __repr__ ici aussi.


if __name__ == "__main__":
    print(lancer_de())
    print(hypotenuse(3, 4))
    print(date_francaise(2026, 7, 16))

    print(Livre("1984", "Orwell", 328))

    compte = CompteBancaire("Ada")
    compte.deposer(100)
    compte.retirer(30)
    print(f"Solde : {compte.solde}")
    try:
        compte.retirer(1000)
    except ValueError as erreur:
        print(f"Refusé : {erreur}")

    panier = Panier()
    panier.ajouter("Café", 2.5)
    panier.ajouter("Livre", 18.9)
    print(f"{len(panier)} articles, total {panier.total():.2f} €")
