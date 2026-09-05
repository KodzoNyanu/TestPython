"""Module 01 — Solutions commentées.

À lire APRÈS avoir cherché. Se tromper puis corriger fait apprendre ;
lire une solution juste ne fait rien apprendre du tout.
"""


def exercice_1():
    print("Bonjour le monde !")


def exercice_2():
    # Le texte contient une apostrophe, donc on entoure de guillemets DOUBLES.
    # Avec des guillemets simples, 'Je m'appelle Ada' se terminerait à l'apostrophe
    # de « m'appelle » et Python ne comprendrait plus la suite.
    print("Je m'appelle Ada")
    print("J'apprends Python")
    print("Et ça commence bien")


def exercice_3():
    # Trois arguments séparés par des virgules : print met une espace entre chacun.
    print("Python", "est", "genial")


def exercice_4():
    # Ici c'est l'inverse de l'exercice 2 : le texte contient des guillemets doubles,
    # donc on l'entoure de guillemets simples. Le langage ne les distingue pas,
    # ce choix ne sert qu'à éviter le conflit.
    print('Elle a dit "bonjour" puis elle est partie')


def exercice_5():
    # 7 * 6 sans guillemets : Python fait le calcul, puis print affiche le résultat.
    # Avec des guillemets, print("7 * 6") afficherait littéralement les caractères 7 * 6.
    # La réponse à la grande question sur la vie, l'univers et le reste (Douglas Adams).
    print(7 * 6)


if __name__ == "__main__":
    exercice_1()
    exercice_2()
    exercice_3()
    exercice_4()
    exercice_5()
