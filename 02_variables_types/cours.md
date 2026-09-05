# Module 02 — Variables et types

## Une variable est une étiquette

Un programme qui ne fait qu'afficher du texte figé ne sert à rien. Il faut pouvoir **retenir**
des valeurs pour les réutiliser. C'est le rôle des variables :

```python
prenom = "Ada"
print(prenom)          # affiche Ada
print("Bonjour", prenom)
```

Le signe `=` ne veut pas dire « égal » au sens mathématique. Il veut dire **« range cette
valeur sous ce nom »**. On lit `prenom = "Ada"` comme « prenom reçoit Ada ». C'est une
opération, pas une affirmation — c'est pourquoi ceci a un sens parfait en programmation
alors que c'est absurde en maths :

```python
compteur = 0
compteur = compteur + 1    # compteur vaut maintenant 1
```

La ligne se lit de droite à gauche : on calcule `compteur + 1` (donc `0 + 1`, soit `1`),
et on range le résultat sous le nom `compteur`, en écrasant l'ancienne valeur.

Une variable peut être réaffectée autant de fois qu'on veut, et changer complètement de
nature au passage. Python ne s'en offusque pas.

## Nommer ses variables

Les règles dures : un nom commence par une lettre ou `_`, ne contient que lettres, chiffres
et `_`, et pas d'espace. `mon prix` est invalide, `mon_prix` est correct.

La convention Python : **tout en minuscules, mots séparés par des underscores**. On écrit
`prix_total`, pas `prixTotal` ni `PrixTotal`.

La vraie règle, celle qui compte : **un nom doit dire ce que la variable contient**. `x`,
`truc`, `data`, `a1` ne disent rien. `prix_ttc`, `nom_client`, `nombre_essais` disent tout.
Vous passerez bien plus de temps à relire du code qu'à l'écrire — le vôtre compris.

## Les types de base

Toute valeur en Python a un **type**, c'est-à-dire une nature qui détermine ce qu'on peut
en faire. Il y en a quatre à connaître pour commencer :

```python
nom = "Ada"          # str   — une chaîne de caractères (du texte)
age = 36             # int   — un entier
taille = 1.68        # float — un nombre à virgule (noté avec un POINT, pas une virgule)
majeure = True       # bool  — un booléen : True ou False, rien d'autre
```

Vous pouvez toujours demander le type d'une valeur :

```python
print(type(age))     # <class 'int'>
```

Attention au piège n°1 des débutants : `"36"` et `36` ne sont **pas** la même chose. Le
premier est du texte qui ressemble à un nombre, le second est un nombre. Regardez :

```python
print(36 + 36)       # 72   — addition de deux nombres
print("36" + "36")   # 3636 — mise bout à bout de deux textes !
```

Le `+` ne fait pas la même chose selon le type. Sur des nombres il additionne ; sur des
chaînes il **concatène**, c'est-à-dire qu'il colle. Et si vous mélangez les deux, Python
refuse net :

```python
print("36" + 36)
# TypeError: can only concatenate str (not "int") to str
```

`TypeError` signifie « tu m'as donné le mauvais type de valeur ». Contrairement à la
`SyntaxError` du module 01, cette erreur-là survient *pendant* l'exécution : le programme
démarre, tourne, puis s'arrête net à cette ligne.

## Convertir d'un type à l'autre

Trois fonctions font le pont entre les types :

```python
int("36")        # 36    — texte  -> entier
str(36)          # "36"  — entier -> texte
float("1.68")    # 1.68  — texte  -> nombre à virgule
int(1.99)        # 1     — TRONQUE, ne fait pas d'arrondi ! (1.99 -> 1)
```

La conversion échoue si elle n'a pas de sens, et le message est clair :

```python
int("bonjour")
# ValueError: invalid literal for int() with base 10: 'bonjour'
```

`ValueError` signifie « le type est bon (c'est bien du texte), mais la valeur n'a aucun sens
pour ce que tu demandes ». Retenez la nuance avec `TypeError`, elle revient tout le temps.

## Les calculs

```python
7 + 2    # 9   addition
7 - 2    # 5   soustraction
7 * 2    # 14  multiplication
7 / 2    # 3.5 division — donne TOUJOURS un float, même si ça tombe juste
7 // 2   # 3   division entière : le quotient, sans le reste
7 % 2    # 1   modulo : le RESTE de la division
7 ** 2   # 49  puissance
```

Deux méritent qu'on s'y arrête, car ils sont partout dans le vrai code. `//` donne le
quotient et `%` donne le reste — ensemble ils répondent à « combien de fois, et il reste
combien ». Le modulo sert en particulier à tester la divisibilité : `n % 2 == 0` veut dire
« n est pair », parce que sa division par 2 ne laisse aucun reste.

Les priorités sont celles des maths (`*` et `/` avant `+` et `-`), et les parenthèses
tranchent : `(2 + 3) * 4` vaut `20`, `2 + 3 * 4` vaut `14`.

Enfin, un raccourci que vous verrez partout :

```python
compteur = 0
compteur += 1     # équivaut exactement à : compteur = compteur + 1
prix *= 2         # marche avec -=, *=, /=, etc.
```

## Les f-strings : afficher proprement

Coller du texte et des variables avec des `+` et des `str()` est vite illisible. Python a
bien mieux : préfixez la chaîne d'un `f`, et mettez vos variables entre accolades.

```python
prenom = "Ada"
age = 36

print(f"{prenom} a {age} ans")           # Ada a 36 ans
print(f"L'an prochain elle aura {age + 1} ans")   # on peut calculer dedans
```

Tout ce qui est entre accolades est évalué puis inséré, converti en texte automatiquement.
C'est la façon moderne et recommandée de construire du texte en Python — utilisez-la
systématiquement.

Bonus qui vous servira au module 09 : on peut demander un format d'affichage après un `:`.

```python
prix = 3.14159
print(f"{prix:.2f} €")     # 3.14 € — arrondi à 2 décimales pour l'AFFICHAGE
```

La variable `prix`, elle, n'a pas changé : seul son affichage est arrondi.

## Parler à l'utilisateur

`input()` met le programme en pause, attend que l'utilisateur tape quelque chose et appuie
sur Entrée, puis renvoie ce qui a été tapé.

```python
prenom = input("Comment t'appelles-tu ? ")
print(f"Enchanté, {prenom} !")
```

**Le point qui piège tout le monde : `input()` renvoie toujours du texte.** Toujours. Même
si l'utilisateur tape `36`, vous récupérez la chaîne `"36"`. Pour calculer avec, il faut
convertir :

```python
age = int(input("Ton âge ? "))       # int(...) autour de input(...)
print(f"Dans 10 ans tu auras {age + 10} ans")
```

Sans le `int(...)`, `age + 10` déclencherait le `TypeError` vu plus haut.

## À retenir

- `=` range une valeur sous un nom ; ça se lit de droite à gauche.
- Quatre types de base : `str`, `int`, `float`, `bool`. `"36"` n'est pas `36`.
- `int()`, `str()`, `float()` convertissent. `TypeError` = mauvais type ; `ValueError` = bon
  type, valeur absurde.
- `/` donne un float, `//` le quotient entier, `%` le reste (`n % 2 == 0` teste la parité).
- Les f-strings (`f"{variable}"`) sont la bonne façon de construire du texte.
- `input()` renvoie **toujours** du texte — convertissez si vous devez calculer.

## À vous

`python exercices.py`, et au travail.
