"""Module 02 — Solutions commentées."""

# --- Exercice 1 ---
ville = "Paris"
habitants = 2100000
densite = 20641.0   # le .0 en fait un float, pas un int — c'est ce qui était demandé

# --- Exercice 2 ---
score = 0
score += 10
score += 10
score += 10
# score += 10 se lit : « prends la valeur actuelle de score, ajoute 10, et range
# le résultat sous le même nom ». C'est l'équivalent exact de score = score + 10.


# --- Exercice 3 ---
def exercice_3():
    # Le f devant les guillemets active les accolades. Sans lui, on afficherait
    # littéralement les caractères {ville} — une erreur classique et silencieuse.
    print(f"{ville} compte {habitants} habitants")


# --- Exercice 4 ---
saisie = "34"


def exercice_4():
    nombre = int(saisie)      # "34" (texte) devient 34 (nombre)
    print(nombre + 8)
    # Sans le int(), saisie + 8 lèverait un TypeError : on ne colle pas
    # un nombre à la suite d'un texte.


# --- Exercice 5 ---
def exercice_5():
    total = 100
    minutes = total // 60     # 1  — le quotient : combien de minutes entières
    secondes = total % 60     # 40 — le reste : ce qui dépasse
    print(f"{minutes} min {secondes} s")


# --- Exercice 6 ---
prix_ht = 19.99
taux_tva = 1.2


def exercice_6():
    prix_ttc = prix_ht * taux_tva     # 23.987999999999996 en réalité
    print(f"{prix_ttc:.2f} EUR")
    # Le :.2f arrondit à l'AFFICHAGE seulement. La variable garde sa précision.
    # (Et si la valeur exacte vous surprend : les float sont stockés en binaire
    # et ne peuvent pas représenter tous les décimaux exactement. C'est vrai dans
    # tous les langages, pas seulement en Python. On vit très bien avec.)


# --- Exercice 7 ---
a = 1
b = 2

# La méthode universelle, valable dans tous les langages : une variable tampon.
temporaire = a    # temporaire vaut 1
a = b             # a vaut 2
b = temporaire    # b vaut 1 — l'ancienne valeur de a, sauvée juste à temps

# Pourquoi « a = b puis b = a » échoue : dès la première ligne, a vaut 2 et
# l'ancienne valeur 1 est PERDUE. La seconde ligne recopie donc 2 dans b, et
# on se retrouve avec a = b = 2.

# Cela dit, Python offre un raccourci que les autres langages n'ont pas :
#     a, b = b, a
# La partie droite est entièrement évaluée AVANT toute affectation, ce qui rend
# le tampon inutile. C'est l'écriture idiomatique — mais il fallait comprendre
# le mécanisme d'abord.


if __name__ == "__main__":
    print(ville, habitants, densite, score)
    exercice_3()
    exercice_4()
    exercice_5()
    exercice_6()
    print(a, b)
