# Module 09 — Projet final : le suivi de dépenses

Vous avez tous les outils. Il est temps de construire quelque chose de complet — pas un
exercice, un vrai petit programme, avec de vraies données qui survivent à sa fermeture.

## Ce qu'on construit

Un gestionnaire de dépenses en ligne de commande :

```
=== MES DÉPENSES ===
1. Ajouter une dépense
2. Lister les dépenses
3. Statistiques
4. Supprimer une dépense
5. Quitter

Votre choix : 3

--- Statistiques ---
Total          : 66.40 €
Nombre         : 3
Dépense moyenne: 22.13 €
Plus grosse    : Train (45.00 €)

Par catégorie :
  transport      45.00 €  #############         67.8%
  loisirs        18.90 €  #####                 28.5%
  sorties         2.50 €  #                      3.8%
```

(Les barres sont en `#` et pas en jolis blocs pleins : la console Windows écrit en cp1252,
et un caractère de dessin y ferait planter le programme avec `UnicodeEncodeError`. Les
accents, eux, passent sans problème.)

Les données sont dans un fichier CSV, rechargé au démarrage. Fermez, rouvrez : tout est là.

## Pourquoi ce projet

Parce qu'il condense tout le cours et qu'il ressemble à du vrai travail : des données
imparfaites qui viennent d'un fichier, des calculs à faire dessus, un humain à qui présenter
le résultat. C'est exactement la forme d'un traitement de données — vous ferez la même chose
en plus gros avec pandas, et sur le web avec une base de données.

| Ce que vous allez utiliser | Vu au module |
|---|---|
| f-strings, formats `:.2f` | 02 |
| conditions, validation | 03 |
| boucles, accumulateurs | 04 |
| listes de dictionnaires, group by | 05 |
| fonctions, `return` | 06 |
| CSV, `try`/`except`, saisie robuste | 07 |
| classes, `raise`, `import` | 08 |

## La méthode : par étapes qui marchent

**Ne construisez jamais tout d'un coup pour tester à la fin.** C'est le meilleur moyen de
se retrouver avec 200 lignes qui plantent quelque part, et aucune idée d'où.

Faites plutôt ceci : à chaque étape, un programme **qui fonctionne**, un peu plus complet
que le précédent. Vous lancez, vous voyez, vous corrigez tout de suite — et vous savez
toujours que le bug est dans ce que vous venez d'écrire.

C'est la façon dont les professionnels travaillent, et ce n'est pas un détail de méthode :
c'est ce qui rend un gros programme réalisable.

Ouvrez `gestionnaire.py` : le squelette est là, avec les étapes dans l'ordre.

---

### Étape 1 — La classe `Depense`

Un libellé, un montant, une catégorie. Le constructeur **refuse** un libellé vide ou un
montant négatif (`raise ValueError`). Ajoutez `__repr__`.

*Test* : créez-en une à la main, affichez-la, et vérifiez qu'un montant négatif est bien
refusé.

### Étape 2 — Aller-retour avec le disque

`charger(chemin)` renvoie une liste de `Depense` ; `sauvegarder(chemin, depenses)` les écrit
en CSV. Fichier absent → liste vide, pas de crash. Ligne illisible → ignorée, le reste
passe (le fichier `depenses_exemple.csv` fourni en contient une exprès).

*Test* : sauvegardez trois dépenses, relancez, rechargez. Vous devez retrouver les mêmes.

C'est l'étape la plus délicate — les données franchissent la frontière entre votre programme
et le monde extérieur, et le CSV ne connaît que du texte.

### Étape 3 — Les calculs

`total(depenses)`, `moyenne(depenses)`, `total_par_categorie(depenses)`,
`plus_grosse(depenses)`. **Aucune de ces fonctions n'affiche quoi que ce soit** : elles
calculent et renvoient. Chacune doit survivre à une liste vide.

*Test* : le fichier a des tests automatiques prêts pour ces fonctions — lancez-les.

### Étape 4 — L'affichage

`afficher_liste(depenses)` et `afficher_statistiques(depenses)`. Ici, et seulement ici, on a
le droit d'appeler `print`.

Cette séparation entre calcul et affichage est le vrai enseignement du projet. Elle vous
permet de tester les calculs automatiquement (module 06), et de changer plus tard la
présentation — un fichier HTML, un graphique — sans toucher à une seule ligne de calcul.

### Étape 5 — Le menu

Une boucle `while` qui affiche les choix, lit la saisie, appelle la bonne fonction, et
recommence jusqu'à « Quitter ». Aucune saisie, si absurde soit-elle, ne doit faire planter le
programme : réutilisez le motif `while True` + `try` du module 07.

Testez-le en tapant n'importe quoi : des lettres au lieu d'un chiffre, un montant avec une
virgule, un champ vide, un numéro de ligne qui n'existe pas. Ce n'est pas de la méchanceté
gratuite — c'est ce que fera le premier utilisateur venu, dans les trente secondes.

---

## Pour aller plus loin

Quand tout marche, choisissez une extension. C'est en ajoutant une fonctionnalité à du code
existant qu'on découvre si on l'avait bien conçu :

- **Une date sur chaque dépense** (`from datetime import date`), et un filtre par mois.
- **La recherche** par mot-clé dans les libellés.
- **Le budget** : un plafond par catégorie, et une alerte quand on le dépasse.
- **L'export** vers un fichier HTML avec les barres du graphique en vraies barres colorées.
- **Les tests** : un fichier `test_gestionnaire.py` qui vérifie automatiquement les calculs.

## Le mot de la fin

Si vous terminez ce projet, vous savez programmer. Pas « les bases de » : vous savez.
Le reste — les bibliothèques, les frameworks, les bases de données — n'est que du
vocabulaire supplémentaire construit sur exactement ce que vous venez de faire.
