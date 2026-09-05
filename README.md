# Cours de Python — du zéro absolu au premier vrai programme

Bienvenue. Ce cours part du principe que vous n'avez **jamais programmé**. Chaque module
se lit en 15–30 minutes, puis se pratique immédiatement : la lecture seule ne fait pas
apprendre à programmer, c'est le clavier qui fait le travail.

## Comment ça marche

Chaque module est un dossier qui contient trois fichiers :

| Fichier | Rôle |
|---|---|
| `cours.md` | La leçon. À lire en premier, en tapant les exemples au fur et à mesure. |
| `exercices.py` | Les exercices à compléter. Il se lance et vous dit ce qui passe ou rate. |
| `solutions.py` | Les corrigés commentés. À ouvrir **après** avoir essayé, pas avant. |

Pour travailler sur un module, ouvrez un terminal dans son dossier et lancez les exercices :

```
cd D:\Python\cours-python\01_premiers_pas
python exercices.py
```

Au premier lancement tout est marqué `RATE` — c'est normal, rien n'est encore écrit. Vous
complétez le fichier, vous relancez, et vous visez le moment où tout affiche `OK`.

Les deux derniers modules sortent de ce moule : le **09** est un projet complet
(`cahier_des_charges.md` + un squelette `gestionnaire.py` à remplir), et le **10** est une
carte des suites possibles, sans exercices.

## Le parcours

| # | Module | Ce que vous saurez faire à la fin |
|---|---|---|
| 01 | Premiers pas | Exécuter un programme, afficher du texte, commenter votre code |
| 02 | Variables et types | Stocker des données, les convertir, dialoguer avec l'utilisateur |
| 03 | Conditions | Faire prendre des décisions à votre programme |
| 04 | Boucles | Répéter un traitement sans copier-coller |
| 05 | Collections | Manipuler des listes et des dictionnaires de données |
| 06 | Fonctions | Découper un programme en morceaux réutilisables |
| 07 | Fichiers et erreurs | Lire/écrire des fichiers sans planter au premier imprévu |
| 08 | Modules et objets | Réutiliser du code existant et structurer le vôtre |
| 09 | Projet final | Un vrai outil de suivi de dépenses, de bout en bout |
| 10 | Pour aller plus loin | Vos prochaines étapes vers la data et le web |

Faites-les dans l'ordre : chaque module s'appuie sur le précédent.

## Ce qu'il vous faut

Python 3.14 est déjà installé sur cette machine — vérifiez avec `python --version`.
Pour écrire du code, n'importe quel éditeur de texte convient, mais VS Code avec
l'extension Python vous donnera la coloration et les erreurs en direct.

## Trois conseils qui font la différence

**Tapez le code, ne le copiez pas.** Les fautes de frappe et les erreurs qu'elles
provoquent sont une part essentielle de l'apprentissage : c'est en lisant des messages
d'erreur qu'on apprend à les décoder.

**Lisez les messages d'erreur en entier, en commençant par la dernière ligne.** Python est
très bavard, mais la dernière ligne dit presque toujours ce qui ne va pas, et l'avant-dernière
dit où.

**Expérimentez à côté.** Ouvrez un terminal, tapez `python`, et essayez vos idées ligne par
ligne. Ce mode interactif est le meilleur bac à sable qui soit — on en sort avec `exit()`.
