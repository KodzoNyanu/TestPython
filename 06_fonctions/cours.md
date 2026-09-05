# Module 06 — Les fonctions

Le moment est venu de lever le mystère. Depuis le module 01, vous écrivez `def exercice_1():`
en faisant confiance. Voici ce que ça veut dire — et pourquoi c'est le concept le plus
important du cours.

## Pourquoi

Une fonction, c'est un **bout de programme auquel on donne un nom**. On l'écrit une fois,
on l'utilise autant qu'on veut. Trois bénéfices, dans l'ordre d'importance :

**On nomme les idées.** `calculer_prix_ttc(19.99)` dit ce que ça fait ; les trois lignes de
calcul correspondantes ne le disent pas. Un programme bien découpé en fonctions se lit
presque comme un résumé de lui-même.

**On ne se répète pas.** Si le taux de TVA change, on corrige à un seul endroit. Le
copier-coller, lui, garantit qu'on oubliera une copie sur cinq.

**On réduit la complexité.** Tant que la fonction fait ce qu'elle promet, on peut l'utiliser
sans se souvenir de comment elle marche. C'est exactement ce que vous faites avec `print`
depuis le début : vous ne savez pas comment il est écrit, et vous n'en avez pas besoin.

## Définir et appeler

```python
def dire_bonjour():
    print("Bonjour !")
    print("Comment allez-vous ?")

dire_bonjour()      # <- ICI seulement, le code s'exécute
dire_bonjour()      # et on peut recommencer
```

`def` **définit** la fonction : Python enregistre la recette sous ce nom, sans rien exécuter.
C'est la ligne `dire_bonjour()`, avec ses parenthèses, qui **appelle** la fonction et
déclenche vraiment le travail.

Cette distinction explique un grand classique du débutant : « j'ai lancé mon fichier et il
ne s'est rien passé ». C'est qu'il contenait une définition, mais aucun appel. Écrire une
recette n'a jamais fait à manger.

## Les paramètres

Une fonction devient utile quand elle travaille sur des données qu'on lui fournit :

```python
def saluer(prenom):
    print(f"Bonjour {prenom} !")

saluer("Ada")       # Bonjour Ada !
saluer("Alan")      # Bonjour Alan !
```

`prenom` est un **paramètre** : une variable qui n'existe qu'à l'intérieur de la fonction, et
qui reçoit la valeur qu'on donne au moment de l'appel. `"Ada"` est l'**argument** — la valeur
réelle. (Le paramètre est l'étiquette sur la boîte, l'argument est ce qu'on met dedans.)

Plusieurs paramètres se séparent par des virgules, et **l'ordre compte** :

```python
def presenter(prenom, age):
    print(f"{prenom} a {age} ans")

presenter("Ada", 36)         # Ada a 36 ans
presenter(36, "Ada")         # 36 a Ada ans — Python obéit sans broncher !
```

Pour éviter ce genre d'accident, on peut nommer les arguments à l'appel. C'est plus long,
mais impossible à confondre, et c'est très recommandé dès qu'une fonction a plus de deux
paramètres :

```python
presenter(prenom="Ada", age=36)
presenter(age=36, prenom="Ada")     # l'ordre n'a plus d'importance
```

## `return` : rendre un résultat

Voici la vraie nouveauté du module, et la plus mal comprise.

```python
def calculer_ttc(prix_ht):
    return prix_ht * 1.2

resultat = calculer_ttc(19.99)     # on récupère la valeur
print(f"{resultat:.2f} €")
print(f"{calculer_ttc(50):.2f} €") # ou on l'utilise directement
```

**`return` n'affiche rien.** Il *renvoie* une valeur à celui qui a appelé la fonction, qui
en fait ce qu'il veut. La différence avec `print` est fondamentale :

```python
def avec_print(prix):
    print(prix * 1.2)        # montre le résultat à l'humain

def avec_return(prix):
    return prix * 1.2        # rend le résultat au programme

x = avec_print(100)          # affiche 120.0, mais x vaut None !
y = avec_return(100)         # n'affiche rien, mais y vaut 120.0
total = y * 2                # possible avec y, impossible avec x
```

Une fonction qui n'a pas de `return` renvoie `None` — « rien ». C'est pourquoi
`x = avec_print(100)` donne `None` : la fonction a affiché quelque chose, mais n'a rien rendu.

**La règle pratique** : une fonction qui *calcule* doit `return`. L'affichage se fait à
l'extérieur, chez l'appelant. Une fonction qui calcule ET affiche est difficile à réutiliser :
le jour où vous voudrez son résultat pour l'écrire dans un fichier plutôt qu'à l'écran, vous
serez coincé. (Nos exercices vous ont fait afficher jusqu'ici uniquement pour que le
vérificateur puisse voir quelque chose — à partir de maintenant, on fait les choses bien.)

Enfin, `return` **arrête immédiatement** la fonction :

```python
def valeur_absolue(nombre):
    if nombre < 0:
        return -nombre       # sort tout de suite
    return nombre            # atteint seulement si nombre >= 0
```

Pas besoin de `else` : si le `return` du `if` s'exécute, la suite n'existe pas.

## Les paramètres par défaut

```python
def saluer(prenom, message="Bonjour"):
    print(f"{message} {prenom} !")

saluer("Ada")                       # Bonjour Ada !
saluer("Ada", "Salut")              # Salut Ada !
saluer("Ada", message="Coucou")     # Coucou Ada !
```

Un paramètre avec une valeur par défaut devient facultatif. Les paramètres obligatoires
doivent venir en premier dans la définition.

⚠️ **Un piège célèbre** : ne mettez jamais une liste ou un dictionnaire comme valeur par
défaut (`def ajouter(element, liste=[])`). Cette liste est créée **une seule fois**, à la
définition, et se retrouve partagée entre tous les appels — avec des effets absurdes. Le
remède standard :

```python
def ajouter(element, liste=None):
    if liste is None:
        liste = []           # une liste NEUVE à chaque appel
    liste.append(element)
    return liste
```

Retenez juste : valeurs par défaut simples (nombre, texte, `True`, `None`), jamais `[]` ni `{}`.

## La portée des variables

Une variable créée dans une fonction **n'existe que là** :

```python
def calculer():
    resultat = 42        # variable LOCALE
    return resultat

calculer()
print(resultat)          # NameError: name 'resultat' is not defined
```

C'est une bonne nouvelle, pas une contrainte : ça garantit qu'une fonction ne peut pas casser
par accident le reste du programme. Chaque fonction travaille dans sa bulle.

L'inverse est vrai : une fonction peut *lire* les variables définies à l'extérieur — mais
ne comptez pas là-dessus. Une fonction qui dépend de variables extérieures invisibles est
imprévisible. **Faites tout entrer par les paramètres et tout sortir par le `return`** ;
votre fonction devient alors une boîte autonome, testable et réutilisable partout.

## La docstring

Une chaîne placée en toute première ligne d'une fonction décrit ce qu'elle fait :

```python
def calculer_ttc(prix_ht, taux=0.2):
    """Renvoie le prix TTC correspondant au prix HT donné.

    taux : taux de TVA en décimal (0.2 pour 20 %).
    """
    return prix_ht * (1 + taux)
```

Ce n'est pas un commentaire ordinaire : Python la conserve, et `help(calculer_ttc)` l'affiche.
C'est la documentation de votre fonction. Prenez l'habitude d'en écrire une dès que le nom
seul ne suffit pas.

## Bien découper

Une bonne fonction fait **une seule chose**, et son nom le dit. Un nom qui contient « et »
(`charger_et_afficher_et_trier`) trahit une fonction qui en cache trois.

```python
def lire_notes():          # une chose : lire
def calculer_moyenne(notes):    # une chose : calculer
def afficher_bulletin(notes, moyenne):    # une chose : afficher
```

Et le nom d'une fonction devrait être un **verbe** : elle fait quelque chose.
`calculer_moyenne`, pas `moyenne_calcul`.

## À retenir

- `def` définit, `nom()` appelle. Une définition sans appel n'exécute rien.
- Les paramètres reçoivent les arguments ; nommer les arguments à l'appel évite les inversions.
- **`return` rend une valeur, `print` affiche du texte.** Ce n'est pas la même chose. Une
  fonction sans `return` renvoie `None`.
- `return` interrompt la fonction sur-le-champ.
- Défauts simples uniquement : jamais `liste=[]`.
- Les variables locales restent locales. Tout entre par les paramètres, tout sort par le
  `return`.
- Une fonction = une responsabilité, nommée par un verbe, documentée par une docstring.

## À vous

`python exercices.py`. À partir d'ici, les exercices testent ce que vos fonctions
**renvoient**, plus ce qu'elles affichent.
