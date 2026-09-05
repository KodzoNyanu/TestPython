"""Module 03 — Solutions commentées."""


# --- Exercice 1 ---
def exercice_1(age):
    if age >= 18:
        print("Majeur")
    else:
        print("Mineur")


# --- Exercice 2 ---
def exercice_2(note):
    # L'ordre décroissant est ce qui rend ce code correct ET court : quand on
    # atteint le deuxième test, on SAIT déjà que la note est sous 16, inutile
    # donc d'écrire `elif note >= 14 and note < 16`.
    if note >= 16:
        print("Très bien")
    elif note >= 14:
        print("Bien")
    elif note >= 12:
        print("Assez bien")
    elif note >= 10:
        print("Passable")
    else:
        print("Insuffisant")


# --- Exercice 3 ---
def exercice_3(nombre):
    if nombre == 0:
        print("zéro")
    elif nombre % 2 == 0:      # reste nul dans la division par 2 => pair
        print("pair")
    else:
        print("impair")
    # Le test de zéro doit venir en PREMIER : 0 % 2 vaut 0, donc zéro passerait
    # pour un nombre pair si on inversait les deux branches.


# --- Exercice 4 ---
def exercice_4(age, permis):
    if age >= 18:
        if permis:
            print("Peut conduire")
        else:
            print("Majeur sans permis")
    else:
        print("Trop jeune")

    # Variante à plat, sans imbrication — plus lisible dès que les cas se multiplient :
    #     if age < 18:
    #         print("Trop jeune")
    #     elif permis:
    #         print("Peut conduire")
    #     else:
    #         print("Majeur sans permis")
    # Elle traite d'abord le cas rejeté, puis n'a plus à se soucier de l'âge.
    # Ce réflexe — « écarter les cas particuliers en premier » — sert toute une carrière.


# --- Exercice 5 ---
def exercice_5(prenom):
    if prenom:                 # une chaîne vide est « fausse », toute autre est « vraie »
        print(f"Bonjour {prenom} !")
    else:
        print("Vous n'avez rien tapé")
    # `if prenom != "":` marcherait aussi, mais `if prenom:` est l'écriture
    # idiomatique en Python. Autant prendre le bon pli tout de suite.


# --- Exercice 6 ---
def exercice_6(note):
    if 0 <= note <= 20:        # équivaut à : note >= 0 and note <= 20
        print("valide")
    else:
        print("invalide")


# --- Exercice 7 ---
def exercice_7(annee):
    # Version imbriquée : elle suit la règle phrase par phrase, dans l'ordre où
    # on l'énonce. C'est la plus facile à vérifier quand on débute.
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                print("bissextile")     # 2000
            else:
                print("commune")        # 1900
        else:
            print("bissextile")         # 2024
    else:
        print("commune")                # 2023

    # Version condensée, strictement équivalente :
    #     if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
    #         print("bissextile")
    #     else:
    #         print("commune")
    # Les parenthèses sont indispensables : sans elles, `and` s'applique avant `or`
    # et 1900 ressortirait bissextile. En cas de doute, parenthésez — c'est gratuit
    # et ça évite d'avoir à réciter les priorités.


if __name__ == "__main__":
    exercice_1(20)
    exercice_2(14)
    exercice_3(7)
    exercice_4(20, True)
    exercice_5("Ada")
    exercice_6(12)
    exercice_7(1900)
