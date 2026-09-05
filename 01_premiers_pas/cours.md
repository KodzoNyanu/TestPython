# Module 01 — Premiers pas

## Ce qu'est un programme

Un programme, c'est une liste d'instructions que l'ordinateur exécute **dans l'ordre**, de
haut en bas, une par une. Rien de plus. Toute la difficulté du métier consiste à décomposer
ce que vous voulez obtenir en instructions assez petites pour que la machine les comprenne.

Python est un langage particulièrement lisible : le code ressemble presque à de l'anglais.
C'est pour ça qu'on l'utilise autant pour débuter — et aussi, accessoirement, pour faire
tourner une bonne partie de la recherche scientifique et des sites web modernes.

## Votre premier programme

Créez un fichier `bonjour.py` et écrivez dedans une seule ligne :

```python
print("Bonjour !")
```

Puis, dans un terminal ouvert sur le dossier du fichier :

```
python bonjour.py
```

Le terminal affiche `Bonjour !`. Vous venez d'écrire, de lancer et d'exécuter un programme.

Décortiquons cette ligne, parce que tout Python est là en miniature :

- `print` est le **nom d'une fonction** — un outil fourni par Python qui sait faire une chose,
  ici afficher du texte à l'écran.
- Les **parenthèses** signifient « exécute cette fonction maintenant ». On dit qu'on
  « appelle » la fonction.
- Ce qui est **entre les parenthèses** est ce qu'on donne à la fonction pour qu'elle travaille.
  On appelle ça un **argument**.
- Les **guillemets** indiquent que `Bonjour !` est du texte brut, et non du code à interpréter.

## Le texte : les chaînes de caractères

Du texte, en programmation, s'appelle une **chaîne de caractères** (en anglais *string*).
Une chaîne s'écrit entre guillemets doubles `"..."` ou simples `'...'` — les deux marchent
à l'identique, choisissez-en un et tenez-vous-y.

```python
print("Avec des guillemets doubles")
print('Avec des guillemets simples')
```

Les guillemets simples sont pratiques quand le texte contient une apostrophe :

```python
print("C'est plus simple comme ça")   # pas de conflit avec l'apostrophe
print('Il a dit "bonjour"')            # pas de conflit avec les guillemets doubles
```

Si vous oubliez un guillemet fermant, Python vous le dira sans détour :

```
SyntaxError: unterminated string literal
```

Cette erreur, `SyntaxError`, signifie « ce que tu as écrit n'est pas du Python valide ».
Le programme ne démarre même pas. Vous la verrez souvent au début — c'est la plus bénigne
de toutes, car elle est détectée avant même que quoi que ce soit ne s'exécute.

## Afficher plusieurs choses

`print` accepte plusieurs arguments, séparés par des virgules. Il les affiche à la suite
en insérant automatiquement une espace entre eux :

```python
print("Bonjour", "le", "monde")
```

affiche `Bonjour le monde`.

Et chaque appel à `print` termine par un passage à la ligne, donc :

```python
print("Première ligne")
print("Deuxième ligne")
```

affiche bien deux lignes distinctes.

## Les commentaires

Tout ce qui suit un `#` sur une ligne est ignoré par Python. C'est un **commentaire** :
du texte écrit pour les humains qui liront le code — vous, dans trois mois, en premier.

```python
# Ce programme salue l'utilisateur
print("Bonjour !")   # un commentaire peut aussi suivre du code
```

Un bon commentaire n'explique pas *ce que* fait le code (le code le dit déjà), il explique
*pourquoi* il le fait. `print("Bonjour")  # affiche Bonjour` n'apporte rien à personne.

## Les erreurs, votre meilleur outil

Provoquez volontairement une erreur, c'est instructif. Tapez :

```python
print("Bonjour"
```

Python répond quelque chose comme :

```
  File "bonjour.py", line 1
    print("Bonjour"
         ^
SyntaxError: '(' was never closed
```

Lisez ce message de bas en haut : **la dernière ligne dit le problème** (une parenthèse
jamais refermée), **les lignes du dessus disent où** (fichier `bonjour.py`, ligne 1) et le
petit `^` pointe l'endroit exact. Prenez tout de suite l'habitude de lire ces messages
au lieu de les subir : ils sont écrits pour vous aider.

## Le mode interactif

Tapez simplement `python` dans un terminal, sans nom de fichier. Vous obtenez une invite `>>>`
où chaque ligne est exécutée dès que vous appuyez sur Entrée :

```
>>> print("Salut")
Salut
>>> 2 + 2
4
```

C'est le brouillon idéal pour tester une idée en trois secondes. On en sort avec `exit()`.
Remarquez qu'en mode interactif, `2 + 2` affiche `4` tout seul, sans `print` — c'est une
commodité de ce mode uniquement. Dans un fichier `.py`, il faut écrire `print(2 + 2)`,
sinon le calcul est fait puis le résultat jeté silencieusement.

## À retenir

- Un programme s'exécute ligne par ligne, de haut en bas.
- `print(...)` affiche à l'écran ; les parenthèses appellent la fonction, l'intérieur est
  ce qu'on lui donne.
- Le texte s'écrit entre guillemets ; c'est une « chaîne de caractères ».
- `#` démarre un commentaire, ignoré par Python.
- Une erreur n'est pas un échec, c'est un message. Lisez-la en commençant par la fin.

## À vous

Ouvrez `exercices.py`, lancez-le une première fois avec `python exercices.py` pour voir
l'état des lieux, puis complétez-le jusqu'à ce que tout affiche `OK`.
