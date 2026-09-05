# Module 04 — Les boucles

Un ordinateur ne se fatigue pas. Ce qu'il fait mieux que nous, c'est répéter la même chose
un million de fois sans se plaindre. Les boucles sont ce qui rend ça possible — et si vous
vous surprenez un jour à copier-coller cinq fois la même ligne, c'est qu'il vous faut une
boucle.

## `for` : répéter un nombre connu de fois

```python
for i in range(5):
    print(i)
```

affiche `0 1 2 3 4`, un par ligne. Décortiquons :

- `range(5)` produit la suite des entiers **de 0 inclus à 5 exclu**, soit 0, 1, 2, 3, 4.
- `for i in ...` prend ces valeurs **une par une** et range chacune dans `i`.
- Le bloc indenté s'exécute une fois par valeur.

Deux surprises pour un débutant, et elles sont liées : **on commence à 0**, et **la borne
finale est exclue**. C'est déroutant deux jours, puis ça devient naturel — et surtout,
`range(5)` donne exactement 5 valeurs, ce qui est bien commode.

`range` accepte jusqu'à trois arguments :

```python
range(5)          # 0, 1, 2, 3, 4          — de 0 à 5 exclu
range(1, 6)       # 1, 2, 3, 4, 5          — de 1 à 6 exclu
range(0, 10, 2)   # 0, 2, 4, 6, 8          — avec un pas de 2
range(5, 0, -1)   # 5, 4, 3, 2, 1          — à l'envers
```

Le nom `i` n'a rien de magique, c'est une variable ordinaire (`i` pour *index*, par
tradition). Si elle a un sens, nommez-la : `for annee in range(2020, 2026):` se lit tout
seul.

## Parcourir directement les choses

Le `for` de Python ne sert pas qu'à compter : il parcourt **tout ce qui contient plusieurs
éléments**. Une chaîne, par exemple, contient des caractères :

```python
for lettre in "Python":
    print(lettre)
```

Une liste (le sujet du module 05) contient des éléments :

```python
for prenom in ["Ada", "Alan", "Grace"]:
    print(f"Bonjour {prenom}")
```

C'est là une vraie différence culturelle avec d'autres langages, où l'on écrit une boucle
sur un indice puis on va chercher l'élément à cet indice. En Python, on prend l'élément
directement. **Si vous vous voyez écrire `for i in range(len(quelque_chose))`, c'est
presque toujours qu'il fallait écrire `for element in quelque_chose`.**

## L'accumulateur

Voici le motif le plus utile de tout ce module. Pour calculer un total, on prépare une
variable **avant** la boucle, et on l'enrichit **à chaque tour** :

```python
total = 0                    # avant : on part de zéro
for prix in [10, 25, 3]:
    total += prix            # pendant : on accumule
print(total)                 # après : 38
```

L'endroit où l'on écrit chaque ligne est le cœur du sujet. `total = 0` doit être **avant**
la boucle : à l'intérieur, il serait remis à zéro à chaque tour et le total final vaudrait
toujours le dernier prix. Et `print(total)` doit être **après**, non indenté : à l'intérieur,
il afficherait les totaux intermédiaires. Le même code, décalé différemment, fait trois
programmes différents. C'est tout Python en une image.

Ce motif se décline : compter (`compteur += 1`), chercher un maximum, construire du texte…
Vous le reconnaîtrez partout.

## `while` : répéter tant qu'une condition tient

Quand on ne sait pas d'avance combien de tours seront nécessaires, on utilise `while` —
« tant que » :

```python
compteur = 3
while compteur > 0:
    print(compteur)
    compteur -= 1        # SANS cette ligne, la boucle tourne à l'infini
print("Partez !")
```

La condition est testée **avant chaque tour**. Si elle est fausse dès le départ, le bloc
n'est jamais exécuté.

Le danger est réel : si rien à l'intérieur ne fait avancer la condition vers `False`, le
programme tourne pour toujours. C'est la **boucle infinie**, l'accident de débutant par
excellence. On s'en sort avec `Ctrl + C`, qui interrompt le programme. Avant de lancer un
`while`, prenez le réflexe de vous demander : *qu'est-ce qui, ici, va finir par rendre la
condition fausse ?*

Le cas typique du `while`, c'est le dialogue avec un utilisateur, dont on ignore par nature
combien de fois il va se tromper :

```python
reponse = ""
while reponse != "oui" and reponse != "non":
    reponse = input("Répondez par oui ou non : ")
print(f"Vous avez dit {reponse}")
```

**Comment choisir ?** Si vous pouvez compter les tours d'avance (« pour chacun des
éléments », « 10 fois »), c'est un `for`. Si l'arrêt dépend de ce qui se passe pendant
(« jusqu'à ce que l'utilisateur… », « tant qu'on n'a pas trouvé »), c'est un `while`.
Dans le doute, `for` — il est plus sûr, il termine toujours.

## `break` et `continue`

`break` sort immédiatement de la boucle :

```python
for nombre in range(100):
    if nombre * nombre > 50:
        print(f"Le premier carré au-dessus de 50 est celui de {nombre}")
        break                # inutile de continuer, on a trouvé
```

`continue` saute au tour suivant sans finir celui-ci :

```python
for nombre in range(10):
    if nombre % 2 == 0:
        continue             # on ignore les pairs
    print(nombre)            # 1 3 5 7 9
```

Ces deux instructions sont utiles mais cassent la lecture linéaire du code. Utilisez-les
quand elles simplifient vraiment, pas par réflexe.

## Boucles imbriquées

Une boucle dans une boucle : pour **chaque** tour de l'extérieure, l'intérieure fait
**tous** ses tours.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")             # après chaque table complète
```

Ça donne 3 × 3 = 9 lignes de calcul. Gardez en tête que le coût se multiplie : deux boucles
de 1000 tours, ça fait un million d'opérations.

## À retenir

- `for element in quelque_chose:` parcourt directement ; `range(n)` va de 0 à n **exclu**.
- Préférez `for element in liste` à `for i in range(len(liste))`.
- L'accumulateur : initialiser **avant** la boucle, accumuler **dedans**, afficher **après**.
  L'indentation décide de tout.
- `while condition:` répète tant que c'est vrai — assurez-vous que quelque chose fasse
  avancer la condition, sinon boucle infinie (`Ctrl + C` pour en sortir).
- Nombre de tours connu → `for`. Arrêt dépendant du déroulé → `while`.
- `break` sort de la boucle, `continue` passe au tour suivant.

## À vous

`python exercices.py`.
