"""Module 06 — Solutions commentées."""


# --- Exercice 1 ---
def carre(nombre):
    return nombre * nombre
    # return, pas print. Avec print, la fonction afficherait 16 puis renverrait
    # None, et `resultat = carre(4) * 2` planterait.


# --- Exercice 2 ---
def calculer_ttc(prix_ht, taux=0.2):
    return prix_ht * (1 + taux)
    # Le paramètre par défaut rend le taux facultatif : calculer_ttc(100) marche,
    # et calculer_ttc(100, 0.055) permet quand même le taux réduit.
    # Rappel : les paramètres obligatoires viennent toujours avant ceux qui ont
    # un défaut, sinon Python refuse la définition.


# --- Exercice 3 ---
def valeur_absolue(nombre):
    if nombre < 0:
        return -nombre     # sort immédiatement de la fonction
    return nombre          # atteint uniquement si nombre >= 0
    # Le else est inutile : si le premier return s'exécute, plus rien ne suit.
    # Ce style « return tôt » évite l'imbrication et se lit très bien.


# --- Exercice 4 ---
def est_bissextile(annee):
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)
    # Une comparaison EST un booléen : on peut la renvoyer telle quelle.
    # Écrire `if condition: return True else: return False` revient à dire
    # « si c'est vrai, renvoie vrai » — c'est du bruit, et tout relecteur
    # expérimenté le signalera.


# --- Exercice 5 ---
def mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    return "Insuffisant"
    # Comparez avec le module 03 : c'est le même code, mais il RENVOIE au lieu
    # d'afficher. Il est donc réutilisable — l'exercice 8 va s'en servir.


# --- Exercice 6 ---
def garder_pairs(nombres):
    pairs = []
    for nombre in nombres:
        if nombre % 2 == 0:
            pairs.append(nombre)
    return pairs
    # On construit une NOUVELLE liste. Supprimer les impairs de la liste reçue
    # modifierait la liste de l'appelant — un effet de bord qu'il n'a pas demandé
    # et qui provoque des bugs très pénibles à retrouver.
    #
    # Python a une écriture condensée pour ce motif, la « compréhension de liste » :
    #     return [n for n in nombres if n % 2 == 0]
    # Vous la croiserez partout. Elle se lit « n pour chaque n dans nombres, si n
    # est pair ». Elle sera au programme du module 10.


# --- Exercice 7 ---
def moyenne(notes):
    if not notes:              # « si la liste est vide » (une liste vide est fausse)
        return None
    return round(sum(notes) / len(notes), 2)
    # Sans le garde-fou, sum([]) / len([]) fait 0 / 0 et lève
    # ZeroDivisionError: division by zero.
    # Traiter le cas limite en premier, puis dérouler le cas normal sans plus
    # y penser : c'est un réflexe qui distingue le code robuste du code fragile.


# --- Exercice 8 ---
def bulletin(notes):
    moy = moyenne(notes)
    if moy is None:
        return None
    return {
        "moyenne": moy,
        "mention": mention(moy),
        "reussi": moy >= 10,
    }
    # Zéro calcul recopié : cette fonction ne fait qu'assembler les précédentes.
    # C'est exactement ce à quoi servent les fonctions. Le jour où les seuils de
    # mention changent, on corrige mention() et bulletin() suit tout seul.
    #
    # On teste `if moy is None:` et non `if not moy:` : une moyenne de 0 est
    # fausse au sens booléen, et confondrait « pas de notes » avec « nul partout ».
    # Pour None, on compare toujours avec `is`.


# --- Exercice 9 ---
def plus_grand(a, b, c):
    """Renvoie le plus grand des trois nombres a, b et c."""
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum
    # Le motif « je prends le premier comme champion provisoire, puis je défie
    # les autres » se généralise à une liste de taille quelconque avec une boucle.
    # C'est très exactement ce que fait max() — que vous utiliserez en vrai.


if __name__ == "__main__":
    print(carre(4))
    print(calculer_ttc(100))
    print(valeur_absolue(-5))
    print(est_bissextile(2024))
    print(mention(14))
    print(garder_pairs([1, 2, 3, 4]))
    print(moyenne([12, 15.5, 8, 20]))
    print(bulletin([12, 15.5, 8, 20]))
    print(plus_grand(1, 3, 2))
    help(plus_grand)      # affiche la docstring
