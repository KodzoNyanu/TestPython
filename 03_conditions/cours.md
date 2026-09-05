# Module 03 — Les conditions

Jusqu'ici vos programmes font toujours exactement la même chose. Un vrai programme, lui,
**décide** : il regarde les données et choisit son chemin. C'est ce qu'on voit ici.

## Comparer

Une comparaison produit un booléen — `True` ou `False`, rien d'autre :

```python
5 > 3       # True
5 < 3       # False
5 >= 5      # True
5 <= 4      # False
5 == 5      # True   — égalité
5 != 5      # False  — différence
```

**`=` et `==` ne sont pas la même chose**, et c'est la confusion n°1 du débutant.
`age = 18` range 18 dans age. `age == 18` demande « est-ce que age vaut 18 ? » et répond
True ou False. Le premier agit, le second interroge.

Les comparaisons marchent aussi sur le texte, où `==` teste l'identité exacte (majuscules
comprises : `"Ada" == "ada"` est `False`) et `<` compare dans l'ordre alphabétique.

## `if` : le premier aiguillage

```python
age = 20

if age >= 18:
    print("Vous êtes majeur")
    print("Bienvenue")
print("Fin du programme")
```

Trois choses à voir, et elles sont toutes essentielles :

**Les deux points `:`** terminent la ligne du `if`. Les oublier est la faute de frappe la
plus fréquente du monde ; Python répond `SyntaxError: expected ':'`.

**L'indentation** — le décalage de 4 espaces — n'est pas de la décoration. Dans la plupart
des langages, on délimite les blocs avec des accolades ; en Python, **c'est le décalage
lui-même qui dit quelles lignes sont à l'intérieur du `if`**. Ici, les deux `print` décalés
ne s'exécutent que si la condition est vraie, tandis que `print("Fin du programme")`, revenu
à gauche, s'exécute toujours. Un décalage mal placé change le sens du programme sans provoquer
la moindre erreur — c'est la source de bugs la plus vicieuse pour un débutant. Utilisez
toujours 4 espaces, et jamais de tabulations.

**La condition** est simplement une expression qui vaut True ou False.

## `else` et `elif`

`else` couvre tous les cas où la condition est fausse :

```python
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

`elif` (contraction de *else if*) enchaîne les possibilités. Python teste les conditions
**dans l'ordre, de haut en bas, et s'arrête à la première qui est vraie** :

```python
note = 14

if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
elif note >= 12:
    mention = "Assez bien"
elif note >= 10:
    mention = "Passable"
else:
    mention = "Insuffisant"

print(mention)     # Bien
```

Cet arrêt à la première condition vraie explique pourquoi l'ordre compte énormément. Si vous
mettiez `note >= 10` en premier, une note de 18 déclencherait « Passable » et les autres
branches ne seraient jamais atteintes. Ce n'est pas une erreur pour Python — juste un
programme faux. Retenez la règle : **du plus restrictif au plus général**.

Notez aussi qu'on n'a pas eu à écrire `elif note >= 14 and note < 16` : si on est arrivé
au deuxième test, c'est que le premier était faux, donc que la note est forcément sous 16.
Les conditions précédentes sont acquises.

## Combiner des conditions

```python
and    # vrai si LES DEUX côtés sont vrais
or     # vrai si AU MOINS UN côté est vrai
not    # inverse
```

```python
age = 25
permis = True

if age >= 18 and permis:
    print("Peut conduire")

if age < 3 or age > 65:
    print("Tarif réduit")

if not permis:
    print("Doit passer le permis")
```

Remarquez `if age >= 18 and permis:` — on n'écrit pas `permis == True`. C'est inutilement
bavard : `permis` *est déjà* un booléen. Écrire `if permis:` se lit d'ailleurs très bien en
français : « si permis ».

Python permet aussi d'enchaîner les comparaisons comme en maths, ce que très peu de langages
autorisent :

```python
if 0 <= note <= 20:      # équivaut à : note >= 0 and note <= 20
    print("Note valide")
```

## Imbriquer

Un `if` peut contenir un autre `if` — on décale simplement d'un niveau de plus :

```python
if age >= 18:
    if permis:
        print("Peut conduire")
    else:
        print("Majeur mais sans permis")
else:
    print("Trop jeune")
```

C'est parfois nécessaire, mais méfiez-vous : au-delà de deux niveaux, le code devient
difficile à suivre. Souvent, un `and` bien placé remplace avantageusement une imbrication.

## Ce qui est vrai, ce qui est faux

Python accepte n'importe quelle valeur comme condition, pas seulement un booléen. Sont
considérés comme **faux** : `False`, `0`, `0.0`, la chaîne vide `""`, la liste vide `[]`
et `None`. **Tout le reste est vrai.**

```python
prenom = input("Ton prénom ? ")

if prenom:                      # se lit « si prénom a été renseigné »
    print(f"Bonjour {prenom}")
else:
    print("Vous n'avez rien tapé")
```

C'est une écriture très idiomatique en Python, et vous la croiserez partout. Elle repose
sur le fait qu'une chaîne vide est « fausse ».

## À retenir

- `=` affecte, `==` compare. Ne les confondez jamais.
- `if condition:` — les deux points, puis l'indentation de 4 espaces qui délimite le bloc.
- `elif` teste dans l'ordre et s'arrête au premier vrai : allez du plus restrictif au plus
  général.
- `and`, `or`, `not` combinent les conditions ; `0 <= x <= 20` est autorisé.
- `if permis:` plutôt que `if permis == True:`.
- Vide ou zéro = faux ; tout le reste = vrai.

## À vous

`python exercices.py`.
