# projetKivy #

## Contexte ##

Projet créé dans le cadre d'un projet cross-dev de [l'iut d'orleans](https://www.univ-orleans.fr/iut-orleans/) Le projet est réalisé avec :


- [Pyhon](https://www.python.org/) (framework cross-dev python)
- [Kivy](https://kivy.org) (framework cross-dev python)

## Installation (requis python 2.7 & pip )##

### Sans virtualenv ###

Installation des dépendcences

    pip install -r requirements.txt

### Avec virtualenv (best practice) ###  

Virtualenv est un systeme d'environement virtuel permetant de bien séparer ses dépencences de projet ( principalement de projet python )

Installation de virtualenv

    pip install --user virtualenv

Création de l'environement

    virtualenv -p python2 ../venvProjetKivy

Activation de l'environement

    source ../venvProjetKivy/bin/activate

Installation des dépendcences

    pip install -r requirements.txt
