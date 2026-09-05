"""Module 05 — Solutions commentées."""

# --- Exercice 1 ---
fruits = ["cerise", "abricot", "banane", "datte"]
fruits.remove("abricot")     # supprime par VALEUR (pas par indice)
fruits.append("fraise")      # ajoute à la fin
fruits.sort()                # trie SUR PLACE, ne renvoie rien
# Piège classique : `fruits = fruits.sort()` remplacerait la liste par None,
# car sort() modifie et ne renvoie rien. Si vous voulez une copie triée sans
# toucher à l'original, c'est `tries = sorted(fruits)`.


# --- Exercice 2 ---
def exercice_2(notes):
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne : {moyenne:.2f}")
    print(f"Minimum : {min(notes)}")
    print(f"Maximum : {max(notes)}")
    # Aucune boucle : sum, len, min et max existent déjà. Réécrire une boucle
    # pour ça, c'est du travail en plus et une occasion de bug en plus.


# --- Exercice 3 ---
def exercice_3(prenoms):
    for indice, prenom in enumerate(prenoms):
        print(f"{indice + 1}. {prenom}")
    # enumerate donne les deux à la fois. Le + 1 est là parce que les indices
    # commencent à 0 mais qu'un humain compte à partir de 1.
    # (Variante : enumerate(prenoms, start=1) fait démarrer le compteur à 1.)


# --- Exercice 4 ---
def exercice_4(nombres):
    print(nombres[:2])       # du début à l'indice 2 exclu
    print(nombres[-2:])      # de l'avant-dernier jusqu'à la fin
    print(nombres[::-1])     # tout, avec un pas de -1 : à l'envers
    # nombres[::-1] crée une COPIE inversée et laisse l'original intact,
    # là où nombres.reverse() modifierait la liste en place. Ici on veut
    # seulement afficher, donc la copie est le bon choix.


# --- Exercice 5 ---
def exercice_5(personne):
    ville = personne.get("ville", "ville inconnue")
    print(f"{personne['prenom']}, {personne['age']} ans, {ville}")
    # personne["ville"] planterait avec KeyError sur la fiche d'Alan.
    # get() renvoie le défaut à la place — c'est fait exactement pour ça.
    # Notez les guillemets simples dans {personne['prenom']} : la f-string est
    # délimitée par des doubles, il ne faut pas la refermer par accident.


# --- Exercice 6 ---
def exercice_6(mots):
    comptes = {}
    for mot in mots:
        comptes[mot] = comptes.get(mot, 0) + 1
        # Se lit : « le compte actuel, ou 0 si le mot est nouveau, plus 1 ».
        # Version longue, strictement équivalente :
        #     if mot in comptes:
        #         comptes[mot] += 1
        #     else:
        #         comptes[mot] = 1

    for mot in sorted(comptes):      # sorted() sur un dict parcourt ses CLÉS triées
        print(f"{mot} : {comptes[mot]}")


# --- Exercice 7 ---
def exercice_7(depenses):
    total = 0
    for depense in depenses:
        print(f"{depense['libelle']} : {depense['montant']:.2f} €")
        total += depense["montant"]
    print(f"Total : {total:.2f} €")
    # Un seul parcours suffit pour afficher ET accumuler. Inutile de faire
    # deux boucles.


# --- Exercice 8 ---
def exercice_8(depenses):
    totaux = {}
    for depense in depenses:
        categorie = depense["categorie"]
        totaux[categorie] = totaux.get(categorie, 0) + depense["montant"]

    for categorie in sorted(totaux):
        print(f"{categorie} : {totaux[categorie]:.2f} €")

    # C'est exactement le compteur de l'exercice 6, à un détail près : on ajoute
    # un montant au lieu de 1. Reconnaître qu'un problème nouveau est un problème
    # déjà résolu sous un autre costume, c'est une bonne part du métier.
    #
    # Ce regroupement s'appelle un « group by ». En data, avec pandas, la même
    # chose s'écrira :  df.groupby("categorie")["montant"].sum()
    # Mais l'avoir écrit à la main une fois change tout : vous saurez ce que
    # la bibliothèque fait pour vous, au lieu de réciter une formule magique.


if __name__ == "__main__":
    depenses = [
        {"libelle": "Café", "montant": 2.5, "categorie": "sorties"},
        {"libelle": "Train", "montant": 45.0, "categorie": "transport"},
        {"libelle": "Livre", "montant": 18.9, "categorie": "loisirs"},
    ]
    print(fruits)
    exercice_2([12, 15.5, 8, 20])
    exercice_3(["Ada", "Alan", "Grace"])
    exercice_4([0, 1, 2, 3, 4, 5])
    exercice_5({"prenom": "Alan", "age": 41})
    exercice_6(["chat", "chien", "chat", "oiseau", "chat"])
    exercice_7(depenses)
    exercice_8(depenses)
