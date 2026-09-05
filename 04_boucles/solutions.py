"""Module 04 — Solutions commentées."""


# --- Exercice 1 ---
def exercice_1():
    # range(1, 6) : 1 inclus, 6 exclu -> 1, 2, 3, 4, 5
    for i in range(1, 6):
        print(i)


# --- Exercice 2 ---
def exercice_2():
    # Trois arguments : départ 5, arrivée 0 (exclue), pas -1.
    # L'arrivée reste exclue même à l'envers : on s'arrête donc bien à 1.
    for i in range(5, 0, -1):
        print(i)
    print("Décollage !")     # après la boucle, donc NON indenté


# --- Exercice 3 ---
def exercice_3():
    total = 0                # AVANT : sinon remis à zéro à chaque tour
    for i in range(1, 101):
        total += i           # DEDANS : on accumule
    print(total)             # APRÈS : sinon on afficherait les 100 totaux intermédiaires


# --- Exercice 4 ---
def exercice_4(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        # On peut calculer directement dans les accolades d'une f-string.


# --- Exercice 5 ---
def exercice_5(mot):
    compteur = 0
    for lettre in mot:              # on parcourt les caractères, pas des indices
        if lettre in "aeiouy":      # ici `in` teste l'appartenance
            compteur += 1
    print(compteur)


# --- Exercice 6 ---
def exercice_6(n):
    for candidat in range(2, n + 1):    # n + 1 pour que n lui-même soit testé
        if n % candidat == 0:
            print(candidat)
            break                        # trouvé : inutile de continuer
    # Pourquoi la boucle trouve toujours quelque chose : tout nombre est divisible
    # par lui-même, donc le dernier candidat (n) marche à coup sûr. C'est ce qui
    # donne 13 pour 13 — un nombre premier n'a pas d'autre diviseur.


# --- Exercice 7 ---
def exercice_7(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:      # le cas le PLUS restrictif en premier
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    # Le piège : si on teste `i % 3 == 0` en premier, 15 affiche « Fizz » et
    # on n'atteint jamais le cas FizzBuzz. Même leçon qu'aux mentions du module 03.
    # (Note : `i % 15 == 0` marche aussi pour le premier test, mais exprime moins
    # clairement l'intention « divisible par 3 ET par 5 ».)


# --- Exercice 8 ---
def exercice_8(hauteur):
    # Version courte : multiplier une chaîne la répète.
    for ligne in range(1, hauteur + 1):
        print("*" * ligne)

    # Version avec boucles imbriquées, pour l'entraînement :
    #     for ligne in range(1, hauteur + 1):
    #         for _ in range(ligne):
    #             print("*", end="")    # end="" empêche le passage à la ligne
    #         print()                    # print vide = passage à la ligne
    # Le `_` est un nom de variable comme un autre, mais par convention il signale
    # « je dois boucler N fois, mais la valeur du compteur ne m'intéresse pas ».
    #
    # Les deux marchent ; la première est meilleure. En Python, la boucle qu'on
    # n'écrit pas est souvent la meilleure — le langage a déjà l'outil.


if __name__ == "__main__":
    exercice_1()
    exercice_2()
    exercice_3()
    exercice_4(7)
    exercice_5("bonjour")
    exercice_6(15)
    exercice_7(15)
    exercice_8(4)
