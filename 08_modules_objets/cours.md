# Module 08 — Modules et objets

Deux sujets pour finir les fondations : **réutiliser le code des autres** (les modules) et
**structurer le vôtre** (les objets).

## Partie 1 — Les modules

Un module, c'est un fichier Python. Rien de plus mystérieux. `import` vous donne accès à son
contenu.

### La bibliothèque standard

Python est livré avec des centaines de modules déjà installés. C'est ce qu'on appelle
« *batteries included* », et c'est une grande partie de la raison de son succès :

```python
import random
print(random.randint(1, 6))          # un dé
print(random.choice(["oui", "non"])) # un élément au hasard

import math
print(math.sqrt(16))     # 4.0
print(math.pi)           # 3.141592653589793
print(math.ceil(4.2))    # 5 — arrondi au-dessus

from datetime import date, datetime
aujourdhui = date.today()
print(aujourdhui)                          # 2026-07-16
print(aujourdhui.strftime("%d/%m/%Y"))     # 16/07/2026 — format français
print(datetime.now().year)

import json
texte = json.dumps({"nom": "Ada"})    # dictionnaire -> texte JSON
donnees = json.loads(texte)           # texte JSON -> dictionnaire
```

Les trois façons d'importer :

```python
import math                    # math.sqrt(16)      — le plus explicite
from math import sqrt          # sqrt(16)           — plus court
from math import *             # NON. Jamais.
```

La troisième déverse tous les noms du module chez vous, écrase silencieusement les vôtres en
cas de collision, et rend impossible de savoir d'où vient une fonction en lisant le code.
Ne l'utilisez pas.

Entre les deux premières, `import math` est préférable : en lisant `math.sqrt(x)` six mois
plus tard, on sait d'où ça vient. Réservez `from ... import ...` aux noms que vous utilisez
sans arrêt.

### Vos propres modules

Si vous écrivez `outils.py` :

```python
# outils.py
def calculer_ttc(prix_ht, taux=0.2):
    return prix_ht * (1 + taux)
```

vous pouvez vous en servir depuis un autre fichier du même dossier :

```python
# programme.py
import outils
print(outils.calculer_ttc(100))
```

### Le fameux `if __name__ == "__main__":`

Vous le voyez depuis le module 01, voici enfin l'explication. Quand Python exécute un fichier,
il lui donne une variable `__name__`. Elle vaut `"__main__"` si le fichier est **lancé
directement**, et le nom du module s'il est **importé**.

```python
def calculer_ttc(prix_ht, taux=0.2):
    return prix_ht * (1 + taux)

if __name__ == "__main__":
    print(calculer_ttc(100))     # ne s'exécute QUE si on lance ce fichier
```

Sans cette protection, `import outils` afficherait `120.0` au passage — parce qu'importer un
module **exécute tout son contenu**. La ligne signifie donc : « ceci n'est là que quand on me
lance directement, pas quand on m'importe ». D'où son usage pour les démos et les tests.

### Installer des modules tiers

Au-delà de la bibliothèque standard, il y a PyPI et ses centaines de milliers de paquets :

```
pip install requests
```

Le jour où vous ferez du data ou du web, ce sera `pip install pandas` ou
`pip install fastapi`. On y reviendra au module 10.

## Partie 2 — Les objets

### Le problème

Reprenons les dépenses du module 05 :

```python
depense = {"libelle": "Café", "montant": 2.5, "categorie": "sorties"}
```

Ça marche, mais rien ne garantit la cohérence : une faute de frappe (`"libele"`) crée
silencieusement une nouvelle clé, un montant négatif passe sans broncher, et les fonctions
qui traitent ces dépenses vivent éparpillées ailleurs dans le code. **Les données sont d'un
côté, les traitements de l'autre.** Une classe rassemble les deux.

### Une classe

```python
class Depense:
    """Une dépense identifiée par un libellé, un montant et une catégorie."""

    def __init__(self, libelle, montant, categorie="divers"):
        self.libelle = libelle
        self.montant = montant
        self.categorie = categorie

    def est_importante(self):
        return self.montant >= 50

    def afficher(self):
        print(f"{self.libelle} : {self.montant:.2f} € ({self.categorie})")
```

Utilisation :

```python
cafe = Depense("Café", 2.5, "sorties")
train = Depense("Train", 45.0, "transport")

print(cafe.libelle)          # Café — un attribut, pas de crochets ni de guillemets
cafe.afficher()              # Café : 2.50 € (sorties)
print(train.est_importante())    # False
```

Le vocabulaire, en trois mots :

- La **classe** est le moule : elle décrit ce qu'est une dépense en général.
- Un **objet** (ou instance) est ce qui sort du moule : `cafe` et `train` sont deux objets
  distincts, chacun avec ses propres valeurs.
- Les **méthodes** sont les fonctions définies dans la classe. Ce sont des fonctions
  ordinaires, à un détail près : leur premier paramètre est `self`.

### `__init__` et `self`

`__init__` est le **constructeur** : Python l'appelle automatiquement quand vous écrivez
`Depense("Café", 2.5)`. Son rôle est de garnir le nouvel objet.

`self` est **l'objet en train d'être manipulé**. Quand vous écrivez `cafe.afficher()`, Python
appelle en réalité `Depense.afficher(cafe)` : `self` reçoit `cafe`. C'est pour ça que `self`
est le premier paramètre de toutes les méthodes, et qu'on ne le passe jamais à l'appel — il
est fourni automatiquement.

`self.libelle = libelle` range la valeur **dans l'objet**, où elle survivra à la fin de la
méthode. Une variable locale ordinaire, elle, disparaîtrait aussitôt. C'est toute la
différence entre `libelle` (le paramètre, éphémère) et `self.libelle` (l'attribut, persistant).

Oublier `self` devant un attribut est l'erreur n°1 du débutant en POO :

```python
def __init__(self, montant):
    montant = montant        # ne fait RIEN d'utile — variable locale perdue à la sortie
```

### `__repr__` : un affichage lisible

Par défaut, afficher un objet donne ceci :

```python
print(cafe)      # <__main__.Depense object at 0x000001F2...>
```

Inutile. La méthode spéciale `__repr__` corrige ça :

```python
class Depense:
    ...
    def __repr__(self):
        return f"Depense({self.libelle!r}, {self.montant})"

print(cafe)      # Depense('Café', 2.5)
```

Les méthodes entourées de doubles underscores (`__init__`, `__repr__`, `__len__`…) sont
appelées par Python lui-même, en réponse à une opération du langage. On les surnomme
« méthodes magiques ». Vous n'avez pas à les appeler : `print` appelle `__repr__` pour vous.

### Valider dans le constructeur

Voici le vrai gain par rapport au dictionnaire :

```python
def __init__(self, libelle, montant, categorie="divers"):
    if not libelle:
        raise ValueError("Le libellé ne peut pas être vide")
    if montant < 0:
        raise ValueError(f"Montant négatif : {montant}")
    self.libelle = libelle
    self.montant = montant
    self.categorie = categorie
```

`raise` lève une erreur volontairement — c'est le pendant du `try/except` du module 07 : là
vous attrapiez, ici vous lancez. Désormais, **il est impossible de fabriquer une dépense
invalide** : le contrôle est à un seul endroit, et il ne peut pas être contourné. Avec un
dictionnaire, il aurait fallu penser à vérifier partout, à chaque création.

Ce principe a un nom — l'objet protège son propre état — et c'est la raison d'être de la POO,
bien plus que la syntaxe.

### `raise` en deux mots

```python
raise ValueError("message qui explique le problème")
```

Levez une erreur dès que votre fonction reçoit quelque chose qu'elle ne peut pas traiter.
C'est **mieux que renvoyer `None`** : `None` se propage silencieusement et explose trois
fonctions plus loin, à un endroit qui n'a rien à voir. Une erreur levée tôt pointe la vraie
cause. « Échouer vite, échouer bruyamment » est un bon principe.

### Faut-il toujours des classes ?

Non — et c'est important. Python n'est pas Java : une fonction est un outil parfaitement
respectable, et une classe à une seule méthode est presque toujours une fonction déguisée.
Prenez une classe quand des données et des comportements vont manifestement ensemble et
qu'il faut protéger leur cohérence. Sinon, des fonctions et des dictionnaires suffisent très
bien.

## À retenir

- `import module` puis `module.fonction()`. Jamais `from module import *`.
- La bibliothèque standard est vaste : `random`, `math`, `datetime`, `json`, `csv`, `pathlib`…
  Cherchez avant d'écrire.
- Importer un fichier **exécute son contenu** — d'où `if __name__ == "__main__":` pour isoler
  ce qui ne doit tourner qu'en lancement direct.
- Une classe est un moule, un objet en sort ; `__init__` construit, `self` désigne l'objet.
- `self.x = x` crée un attribut durable ; sans `self`, la valeur est perdue.
- Valider dans `__init__` avec `raise` rend les objets invalides impossibles.
- Une classe par défaut, non. Une classe quand données et comportements sont indissociables.

## À vous

`python exercices.py`. C'est le dernier module de fondations — ensuite, le projet.
