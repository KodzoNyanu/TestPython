# Module 10 — Pour aller plus loin

Vous avez fini les fondations. Ce module n'a pas d'exercices : c'est une carte. Il vous
montre ce qui existe juste après, et par où entrer selon ce que vous voulez faire — data
ou web, les deux directions que vous aviez citées au départ.

## D'abord, du Python qui vous manque encore

Trois choses courantes qu'on croise dès qu'on lit du code écrit par d'autres.

### Les compréhensions de liste

Vous avez écrit ceci au module 06 :

```python
pairs = []
for nombre in nombres:
    if nombre % 2 == 0:
        pairs.append(nombre)
```

Les Pythonistes écrivent :

```python
pairs = [nombre for nombre in nombres if nombre % 2 == 0]
```

Ça se lit « nombre, pour chaque nombre de nombres, si nombre est pair ». Même résultat, une
ligne, et c'est **l'écriture attendue** : sur une revue de code, la version longue vous
vaudra une remarque. Ça marche aussi pour transformer, et pour les dictionnaires :

```python
carres = [n ** 2 for n in range(10)]
majuscules = [mot.upper() for mot in mots]
longueurs = {mot: len(mot) for mot in mots}
```

La limite est claire : dès qu'il faut deux conditions imbriquées ou une logique un peu
touffue, revenez à la boucle. Une compréhension illisible est pire qu'une boucle explicite.

### Les f-strings avancées et les méthodes de chaîne

```python
"  Bonjour  ".strip()          # "Bonjour"
"Bonjour".lower()              # "bonjour"
"a,b,c".split(",")             # ["a", "b", "c"]
"-".join(["a", "b", "c"])      # "a-b-c"
"Bonjour".replace("j", "J")    # "BonJour"
"Bonjour".startswith("Bon")    # True
"2026-07-16".split("-")        # ["2026", "07", "16"]
```

`split` et `join` sont réciproques, et ils font l'essentiel du traitement de texte. Vous les
utiliserez tous les jours.

### Les annotations de type

Vous verrez souvent ceci :

```python
def calculer_ttc(prix_ht: float, taux: float = 0.2) -> float:
    return prix_ht * (1 + taux)
```

Ce sont des **annotations** : elles disent quels types sont attendus et renvoyés. Python ne
les vérifie pas à l'exécution — elles ne changent rien au comportement. Elles servent à votre
éditeur (qui vous prévient de vos erreurs en direct), aux relecteurs, et à des outils comme
`mypy`. Sur un projet sérieux, c'est devenu la norme. Adoptez-les quand vous serez à l'aise.

## Les outils du métier

**`venv` — un environnement par projet.** Si le projet A veut pandas 1.5 et le projet B
pandas 2.0, installer tout sur la machine crée un conflit insoluble. Un environnement
virtuel donne à chaque projet ses propres bibliothèques, isolées :

```
python -m venv .venv
.venv\Scripts\activate        # sous Windows
pip install pandas
pip freeze > requirements.txt  # la liste exacte, pour reproduire ailleurs
```

Prenez le pli dès votre premier vrai projet. Ce n'est pas une subtilité d'expert, c'est
l'hygiène de base — et personne ne regrette de l'avoir fait, tout le monde regrette de ne
pas l'avoir fait.

**Git** — pour garder l'historique de votre code et travailler à plusieurs. Indispensable
dès que ça devient sérieux.

**pytest** — pour tester automatiquement. Vous avez déjà l'idée : les vérificateurs de ce
cours sont des tests. Avec pytest, ça s'écrit :

```python
def test_total():
    assert total([]) == 0
```

et `pytest` trouve et lance tout seul chaque fonction nommée `test_*`.

## Direction data

C'est la voie royale de Python — le langage y est dominant, et vos bases suffisent pour
commencer aujourd'hui.

**`pandas`** manipule des tableaux de données. Souvenez-vous du module 05 et de votre projet :
une liste de dictionnaires. Un DataFrame pandas, c'est ça, avec vingt ans d'optimisation
autour.

```python
import pandas as pd

df = pd.read_csv("depenses.csv")
print(df.head())                                  # les 5 premières lignes
print(df["montant"].sum())                        # votre fonction total()
print(df.groupby("categorie")["montant"].sum())   # votre total_par_categorie()
print(df[df["montant"] > 20])                     # filtrer
```

Regardez bien la ligne `groupby` : c'est **exactement** l'exercice 8 du module 05, celui que
vous avez écrit à la main avec un dictionnaire et une boucle. C'est pour ça qu'on vous l'a
fait faire — vous savez ce que la bibliothèque fait à votre place, au lieu de réciter une
incantation.

**`matplotlib`** pour les graphiques, **`numpy`** pour le calcul numérique, **`jupyter`**
pour travailler dans un carnet interactif où code, résultats et graphiques cohabitent
(c'est l'outil standard de l'exploration de données).

**Par où commencer** : reprenez votre projet du module 09 et refaites les statistiques avec
pandas. Trente lignes deviendront trois. Vous ressentirez immédiatement ce que la
bibliothèque apporte — et vous comprendrez ce qu'elle fait, ce qui est rare.

```
pip install pandas matplotlib jupyter
```

## Direction web

**`requests`** consomme des API. C'est le point d'entrée le plus gratifiant :

```python
import requests

reponse = requests.get("https://api.github.com/users/python")
if reponse.status_code == 200:       # 200 = OK
    donnees = reponse.json()         # le JSON devient un dictionnaire Python
    print(donnees["public_repos"])
```

`reponse.json()` rend un dictionnaire — encore la structure du module 05. Tout se recoupe.

**`FastAPI`** crée une API. C'est le framework moderne de référence, et il utilise justement
les annotations de type vues plus haut :

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/depenses")
def lister_depenses():
    return [{"libelle": "Café", "montant": 2.5}]
```

Lancez `uvicorn main:app --reload`, ouvrez `http://localhost:8000/depenses`, et vous avez une
API. Mieux : `http://localhost:8000/docs` vous donne une documentation interactive générée
toute seule. Le `@app.get(...)` est un **décorateur** — le prochain concept Python à
apprendre.

**Django** pour un site complet avec base de données et interface d'administration ;
**Flask** pour quelque chose de plus léger que Django et de plus classique que FastAPI.

**Par où commencer** : exposez votre gestionnaire de dépenses en API avec FastAPI. Vos
fonctions `total()` et `total_par_categorie()` sont déjà prêtes — c'est précisément parce
que vous aviez séparé le calcul de l'affichage qu'elles se réutilisent telles quelles. Vous
n'aurez qu'à remplacer le menu par des routes.

```
pip install requests fastapi uvicorn
```

## Comment continuer à progresser

**Écrivez du code.** Lire des cours donne l'illusion de comprendre ; seul le clavier fait
apprendre. Une heure de code vaut cinq heures de vidéos.

**Ayez un projet qui vous tient à cœur.** Suivre des tutoriels indéfiniment mène à
l'épuisement. Un besoin réel, même minuscule — renommer des photos, suivre un budget,
récupérer des données d'un site — vous fera apprendre trois fois plus vite, parce que vous
voudrez vraiment le résultat.

**Lisez la documentation officielle.** `docs.python.org/fr/` existe en français. C'est plus
sec qu'un tutoriel, mais c'est exact, complet et à jour — trois qualités rares.

**Lisez du code des autres.** Les projets open source sur GitHub sont une mine. Vous n'y
comprendrez pas tout au début : ce n'est pas grave, c'est même le principe.

**Apprenez à chercher.** « python comment trier un dictionnaire par valeur » vous mènera
sur Stack Overflow, où la réponse existe déjà. Ce n'est pas de la triche, c'est le métier.
Mais **comprenez avant de coller** — du code copié sans être compris est une dette qui se
paie au premier bug. C'est vrai des réponses de Stack Overflow comme de celles d'une IA :
l'outil qui vous donne la réponse ne vous donne pas le jugement pour l'évaluer, et c'est ce
jugement que vous venez de passer neuf modules à construire.

**Acceptez d'être bloqué.** Tout le monde l'est, tous les jours, y compris après vingt ans.
La différence n'est pas dans le fait de buter, mais dans les méthodes pour se débloquer :
lire l'erreur en entier, réduire le problème au plus petit exemple qui plante, afficher les
valeurs intermédiaires, expliquer le bug à voix haute à quelqu'un — ou à un canard en
plastique, la méthode a un nom et elle fonctionne vraiment.

## La carte, en une image

```
        VOUS ÊTES ICI
             │
   Les bases : variables, conditions, boucles,
   collections, fonctions, fichiers, objets
             │
      ┌──────┴───────┐
      │              │
    DATA            WEB
   pandas         requests
   numpy          FastAPI / Django
   matplotlib     bases de données (SQL)
   jupyter        HTML / CSS
      │              │
      └──────┬───────┘
             │
   Le métier : git, tests, venv,
   revue de code, déploiement
```

Bonne route. Et n'oubliez pas la seule règle qui compte vraiment : **écrivez du code.**
