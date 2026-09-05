# Module 07 — Fichiers et gestion des erreurs

Jusqu'ici, tout ce que vos programmes calculaient disparaissait à la fermeture. On va y
remédier — et comme le monde extérieur est imprévisible (fichiers absents, données
corrompues, utilisateurs créatifs), on va aussi apprendre à ne pas s'écrouler au premier
imprévu. Les deux sujets vont ensemble : dès qu'on touche à l'extérieur, ça peut rater.

## Lire un fichier

```python
with open("notes.txt", encoding="utf-8") as fichier:
    contenu = fichier.read()

print(contenu)
```

Trois choses à comprendre dans cette ligne.

**`with`** garantit que le fichier sera refermé quoi qu'il arrive — même si une erreur
survient au milieu. Sans lui, il faudrait penser à appeler `fichier.close()`, et le fichier
resterait ouvert en cas de plantage. `with`, toujours. Il n'y a pas de bonne raison de faire
autrement.

**`encoding="utf-8"`** dit comment traduire les octets du disque en caractères. C'est le seul
paramètre optionnel que je vous demande de ne jamais omettre : sans lui, Python utilise
l'encodage par défaut de la machine, qui n'est pas le même sous Windows et sous Linux. Votre
fichier plein d'accents s'ouvrira très bien chez vous et lèvera un `UnicodeDecodeError` chez
votre collègue. Précisez `utf-8` partout, et le problème n'existe plus.

**L'indentation** délimite la zone où le fichier est ouvert. Dès qu'on ressort du bloc, il est
fermé — `contenu`, lui, reste disponible.

### Trois façons de lire

```python
contenu = fichier.read()          # tout, dans une seule chaîne
lignes = fichier.readlines()      # une liste de lignes
for ligne in fichier:             # ligne par ligne — la meilleure
    print(ligne.strip())
```

La troisième est la bonne par défaut : elle ne charge qu'une ligne à la fois en mémoire, donc
elle marche aussi bien sur un fichier de 10 Go que sur trois lignes.

`strip()` mérite une explication : chaque ligne lue se termine par un caractère de saut de
ligne invisible (`\n`), et `strip()` enlève les espaces et sauts de ligne au début et à la
fin. Sans lui, vos comparaisons échouent mystérieusement, parce que `"oui\n" != "oui"`.

## Écrire un fichier

```python
with open("resultat.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Première ligne\n")     # le \n est à VOUS de le mettre
    fichier.write("Deuxième ligne\n")
```

Le deuxième argument est le **mode** :

| Mode | Effet |
|---|---|
| `"r"` | lecture (le défaut) — erreur si le fichier n'existe pas |
| `"w"` | écriture — **écrase intégralement** le fichier existant, ou le crée |
| `"a"` | ajout (*append*) — écrit à la fin, garde le contenu existant |

⚠️ **`"w"` vide le fichier sans rien demander.** Pas de confirmation, pas de corbeille. C'est
la façon la plus rapide de perdre des données quand on débute. Quand vous voulez ajouter,
c'est `"a"`.

Contrairement à `print`, `write` n'ajoute pas de saut de ligne : à vous d'écrire `\n`.

## Le format CSV

Un CSV est un tableau en texte brut, une ligne par enregistrement, des colonnes séparées par
des virgules ou des points-virgules. C'est le format d'échange universel des données — Excel,
les banques, les exports de n'importe quel logiciel. Python a un module dédié :

```python
import csv

# Lecture — chaque ligne devient un dictionnaire, les en-têtes servent de clés
with open("depenses.csv", encoding="utf-8", newline="") as fichier:
    lecteur = csv.DictReader(fichier)
    depenses = list(lecteur)

print(depenses[0]["libelle"])
```

Vous reconnaissez la structure du module 05 : **une liste de dictionnaires**. C'est bien la
même chose, et c'est pour ça qu'on a insisté dessus.

```python
# Écriture
with open("sortie.csv", "w", encoding="utf-8", newline="") as fichier:
    redacteur = csv.DictWriter(fichier, fieldnames=["libelle", "montant"])
    redacteur.writeheader()
    redacteur.writerows(depenses)
```

Le `newline=""` est une bizarrerie que le module csv exige ; sans lui, vous obtenez une ligne
vide sur deux sous Windows. Écrivez-le sans chercher à comprendre.

**Le piège qui compte** : tout ce qui sort d'un CSV est du **texte**, y compris les nombres.
`depense["montant"]` vaut `"2.5"`, pas `2.5`. C'est le `input()` du module 02 qui revient :
convertissez avec `float(...)` avant de calculer, sinon `TypeError`.

## Quand ça tourne mal : `try` / `except`

Vous avez déjà croisé plusieurs erreurs. Jusqu'ici, elles arrêtaient le programme net. On peut
les **attraper** :

```python
try:
    age = int(input("Votre âge : "))
    print(f"Vous avez {age} ans")
except ValueError:
    print("Ce n'est pas un nombre entier.")
```

Python essaie le bloc `try`. Si tout va bien, `except` est ignoré. Si une `ValueError` surgit,
l'exécution saute immédiatement dans le `except` — et le programme continue, au lieu de mourir.

Les erreurs qu'on rencontre le plus :

| Erreur | Cause typique |
|---|---|
| `ValueError` | `int("bonjour")` — bon type, valeur impossible |
| `TypeError` | `"3" + 3` — mauvais type |
| `FileNotFoundError` | le fichier demandé n'existe pas |
| `KeyError` | clé absente d'un dictionnaire |
| `IndexError` | indice hors des limites d'une liste |
| `ZeroDivisionError` | division par zéro |

### La règle d'or

**Attrapez toujours une erreur précise.** Ceci est un piège :

```python
try:
    traiter_les_donnees()
except:            # NON : attrape absolument tout
    print("Erreur")
```

Ce code avale aussi vos fautes de frappe (`NameError`), vos bugs de logique, et même le
`Ctrl + C` de l'utilisateur. Vous croyez gérer une erreur ; en réalité vous les cachez toutes,
y compris celles que vous auriez voulu voir. Le programme continue dans un état incohérent et
vous cherchez pendant des heures.

```python
try:
    with open("donnees.csv", encoding="utf-8") as fichier:
        ...
except FileNotFoundError:
    print("Le fichier donnees.csv est introuvable.")
```

Ici on dit exactement ce qu'on sait gérer. Tout le reste continue de remonter bruyamment,
et c'est très bien : **une erreur que vous n'attendiez pas doit faire du bruit**, pas être
étouffée.

### Les compléments

```python
try:
    fichier = open("donnees.csv", encoding="utf-8")
except FileNotFoundError:
    print("Introuvable")
except PermissionError:              # plusieurs except possibles
    print("Accès refusé")
else:
    print("Ouvert avec succès")      # si AUCUNE erreur n'est survenue
finally:
    print("Terminé")                 # TOUJOURS, erreur ou pas
```

Et si le message de l'erreur vous intéresse :

```python
except ValueError as erreur:
    print(f"Saisie invalide : {erreur}")
```

## Le motif « saisie robuste »

Combinez `while` et `try`, et vous obtenez un dialogue qu'aucune saisie ne peut casser :

```python
def demander_entier(question):
    """Redemande jusqu'à obtenir un entier valide."""
    while True:                      # boucle infinie... 
        try:
            return int(input(question))   # ...dont le return est la sortie
        except ValueError:
            print("Merci de saisir un nombre entier.")
```

`while True` boucle sans fin, et c'est voulu : le `return` est la seule porte de sortie, et
il ne s'ouvre que sur une saisie valide. Si `int()` échoue, on affiche le rappel et on
repart pour un tour. Ce petit bloc est du vrai code de production — gardez-le sous la main.

## Les chemins de fichiers

Sous Windows, les chemins s'écrivent avec des `\`, qui est aussi le caractère d'échappement
de Python : `"C:\notes\test.txt"` contient en réalité un `\n` (saut de ligne) et un `\t`
(tabulation). Deux solutions propres :

```python
chemin = r"C:\Users\admin\notes.txt"     # le r désactive les échappements
chemin = "C:/Users/admin/notes.txt"      # les / marchent aussi sous Windows
```

Et l'outil moderne, qui gère tout ça pour vous et fonctionne à l'identique sur les trois
systèmes :

```python
from pathlib import Path

fichier = Path("donnees") / "depenses.csv"     # le / construit le chemin
if fichier.exists():
    contenu = fichier.read_text(encoding="utf-8")
```

## À retenir

- `with open(..., encoding="utf-8") as f:` — toujours `with`, toujours l'encodage.
- Mode `"w"` **écrase sans prévenir** ; `"a"` ajoute à la fin.
- Parcourez un fichier ligne par ligne, et `strip()` chaque ligne pour ôter le `\n`.
- `csv.DictReader` rend une liste de dictionnaires — mais **tout est du texte**, convertissez.
- `try` / `except ErreurPrécise:` — jamais de `except:` nu.
- `while True` + `try` + `return` = saisie utilisateur incassable.

## À vous

`python exercices.py`. Ce module crée et lit de vrais fichiers, dans un sous-dossier
`bac_a_sable/` — vous pouvez le supprimer sans crainte à tout moment.
