# Module 05 — Listes, dictionnaires et compagnie

Une variable retient **une** valeur. Mais la vraie vie manipule des ensembles : les 30 élèves
d'une classe, les dépenses du mois, les mots d'une phrase. Créer `eleve_1`, `eleve_2`,
`eleve_3`… serait absurde. Il faut des structures de données.

## Les listes

Une liste est une **suite ordonnée** d'éléments, entre crochets :

```python
prenoms = ["Ada", "Alan", "Grace"]
notes = [12, 15.5, 8, 20]
melange = ["Ada", 36, True]     # possible, mais rarement une bonne idée
vide = []
```

### Accéder par indice

```python
print(prenoms[0])     # Ada    — le PREMIER est à l'indice 0
print(prenoms[2])     # Grace
print(prenoms[-1])    # Grace  — le dernier, en comptant depuis la fin
print(prenoms[-2])    # Alan
print(len(prenoms))   # 3      — le nombre d'éléments
```

**On compte à partir de 0.** Le premier élément est à l'indice 0, donc le dernier d'une liste
de 3 éléments est à l'indice 2, pas 3. Demander `prenoms[3]` déclenche :

```
IndexError: list index out of range
```

Les indices négatifs partent de la fin : `[-1]` est le dernier. C'est très pratique, et
bien plus lisible que `prenoms[len(prenoms) - 1]`.

### Modifier

Contrairement aux chaînes, une liste est **modifiable** :

```python
prenoms[1] = "Alan Turing"       # remplace un élément
prenoms.append("Katherine")      # ajoute à la fin
prenoms.insert(0, "Linus")       # insère à l'indice 0, décale le reste
prenoms.remove("Ada")            # supprime la première occurrence de cette VALEUR
dernier = prenoms.pop()          # retire le dernier ET le renvoie
prenoms.sort()                   # trie sur place, la liste est modifiée
prenoms.reverse()                # inverse sur place
```

Le point sur lequel tout le monde trébuche une fois : `append`, `sort` et `reverse` modifient
la liste **et ne renvoient rien**. Donc `prenoms = prenoms.sort()` détruit votre liste en la
remplaçant par `None`. On écrit `prenoms.sort()`, point final. (Si vous voulez une copie triée
sans toucher à l'original, c'est `sorted(prenoms)`.)

### Parcourir

```python
for prenom in prenoms:
    print(prenom)
```

Et si vous avez besoin de l'indice **en plus** de la valeur, `enumerate` vous donne les deux :

```python
for indice, prenom in enumerate(prenoms):
    print(f"{indice + 1}. {prenom}")     # 1. Ada  /  2. Alan  ...
```

### Découper (*slicing*)

```python
nombres = [0, 1, 2, 3, 4, 5]
nombres[1:4]     # [1, 2, 3]     — de 1 inclus à 4 exclu (toujours la même règle)
nombres[:3]      # [0, 1, 2]     — depuis le début
nombres[3:]      # [3, 4, 5]     — jusqu'à la fin
nombres[-2:]     # [4, 5]        — les deux derniers
nombres[:]       # une COPIE complète
```

Ça marche aussi sur les chaînes : `"Python"[:3]` vaut `"Pyt"`.

### Les outils tout faits

```python
notes = [12, 15.5, 8, 20]
len(notes)          # 4
sum(notes)          # 55.5
min(notes)          # 8
max(notes)          # 20
sum(notes) / len(notes)     # 13.875 — la moyenne
15.5 in notes       # True — teste l'appartenance
notes.count(8)      # 1    — compte les occurrences
```

Vous n'avez pas à écrire une boucle pour faire une somme. Le réflexe « il existe sûrement
déjà un outil » vous fera gagner des années.

## Les tuples

Un tuple, c'est une liste **non modifiable**, écrite avec des parenthèses :

```python
point = (3, 5)
x, y = point         # « déballage » : x vaut 3, y vaut 5
point[0] = 10        # TypeError: 'tuple' object does not support item assignment
```

À quoi bon une liste qu'on ne peut pas modifier ? Précisément à ça : garantir que ça ne
bougera pas. On l'utilise pour des ensembles de valeurs qui forment un tout cohérent — des
coordonnées, une date, un couple (nom, prix) — là où une liste sert à une collection
d'éléments de même nature, appelée à grandir et rétrécir.

## Les dictionnaires

C'est probablement la structure la plus utile de Python. Au lieu d'accéder par position, on
accède par **clé** :

```python
personne = {
    "prenom": "Ada",
    "age": 36,
    "ville": "Londres",
}

print(personne["prenom"])       # Ada
personne["age"] = 37            # modifie
personne["email"] = "a@b.c"     # ajoute une nouvelle clé
del personne["ville"]           # supprime
```

Comparez avec une liste : `personne[0]` ne dit rien de ce qu'on récupère, alors que
`personne["prenom"]` est limpide. Dès que vos données ont des champs nommés, prenez un
dictionnaire.

Accéder à une clé absente lève une `KeyError`. Pour éviter le crash, `get` renvoie une valeur
par défaut au lieu de planter :

```python
print(personne["telephone"])           # KeyError: 'telephone'
print(personne.get("telephone"))       # None — pas de crash
print(personne.get("telephone", "non renseigné"))   # non renseigné
print("age" in personne)               # True — teste la présence d'une CLÉ
```

### Parcourir un dictionnaire

```python
for cle in personne:                       # les clés
    print(cle)

for cle, valeur in personne.items():       # les deux à la fois — le plus utile
    print(f"{cle} : {valeur}")

for valeur in personne.values():           # les valeurs seules
    print(valeur)
```

### Le motif qui sert partout : compter

```python
mots = ["chat", "chien", "chat", "oiseau", "chat"]
comptes = {}

for mot in mots:
    if mot in comptes:
        comptes[mot] += 1
    else:
        comptes[mot] = 1        # première rencontre : on initialise à 1

print(comptes)      # {'chat': 3, 'chien': 1, 'oiseau': 1}
```

Le `if` est indispensable : sans lui, `comptes[mot] += 1` sur un mot jamais vu lèverait une
`KeyError`, puisqu'on ne peut pas ajouter 1 à quelque chose qui n'existe pas. La version
compacte du même motif utilise `get` avec un défaut :

```python
comptes[mot] = comptes.get(mot, 0) + 1
```

qui se lit : « prends le compte actuel, ou 0 s'il n'y en a pas, ajoute 1, et range ».

## Combiner les structures

C'est là que ça devient puissant. Une liste de dictionnaires est **la** façon de représenter
un tableau de données — et c'est exactement ce que vous manipulerez en data ou en web :

```python
depenses = [
    {"libelle": "Café", "montant": 2.5, "categorie": "sorties"},
    {"libelle": "Train", "montant": 45.0, "categorie": "transport"},
    {"libelle": "Livre", "montant": 18.9, "categorie": "loisirs"},
]

for depense in depenses:
    print(f"{depense['libelle']:10} {depense['montant']:6.2f} €")

total = 0
for depense in depenses:
    total += depense["montant"]
print(f"Total : {total:.2f} €")
```

Notez les guillemets simples dans `{depense['libelle']}` : la f-string est délimitée par des
doubles, donc à l'intérieur on prend des simples pour ne pas la couper.

## Les ensembles, en deux lignes

Un `set` est une collection **sans doublons et sans ordre** :

```python
set([1, 2, 2, 3, 3, 3])      # {1, 2, 3} — les doublons disparaissent
```

C'est l'outil du dédoublonnage. `list(set(ma_liste))` supprime les doublons d'une liste
(au prix de l'ordre). Ça suffira pour l'instant.

## Laquelle choisir ?

| Besoin | Structure |
|---|---|
| Une suite d'éléments de même nature, ordonnée, qui évolue | **liste** `[]` |
| Des valeurs figées qui forment un tout | **tuple** `()` |
| Des données avec des champs nommés | **dictionnaire** `{}` |
| Des valeurs uniques, sans ordre | **set** |

## À retenir

- Les listes s'indexent à partir de **0** ; `[-1]` est le dernier ; `IndexError` = hors limites.
- `append`, `sort`, `reverse` modifient sur place et ne renvoient rien : jamais
  `liste = liste.sort()`.
- `len`, `sum`, `min`, `max`, `in` existent déjà — ne réécrivez pas de boucle pour ça.
- Le dictionnaire accède par clé ; `get(cle, defaut)` évite la `KeyError` ;
  `.items()` parcourt clés et valeurs ensemble.
- Une **liste de dictionnaires** représente un tableau de données. C'est le motif central.

## À vous

`python exercices.py`.
