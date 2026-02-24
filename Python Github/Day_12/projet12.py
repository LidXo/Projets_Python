# MODULES
'''Un module est un fichier contenant un ensemble de codes ou un ensemble de fonctions qui peuvent être inclus dans une application.
Un module peut être un fichier contenant une seule variable, une fonction ou une grande base de code.'''
# CREATION
'''# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname'''

# IMPORTER UN MODULE
import mymodule
# print(mymodule.generate_full_name('John', 'Doe'))

# Import Functions from a Module
'''from mymodule import generate_full_name, sum_two_nums, person, garvity
print(generate_full_name('John', 'Doe'))
print(sum_two_nums(1, 2))
print(weight)
print(person)

# Import Functions from a Module and Renaming
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])'''

# Importer des modules intégrés
# OS Module
'''Le module os de Python permet d'effectuer automatiquement de nombreuses tâches du système d'exploitation. Le module OS de Python fournit des fonctions permettant de créer, modifier le répertoire de travail actuel et supprimer un répertoire (dossier), récupérer son contenu, modifier et identifier le répertoire actuel.'''
'''import os
os.mkdir('Lidao')'''
# Sys Module
import sys
'''Le module sys fournit des fonctions et des variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python. La fonction sys.argv renvoie une liste des arguments de ligne de commande passés à un script Python. L'élément à l'index 0 de cette liste est toujours le nom du script, tandis que l'élément à l'index 1 est l'argument passé depuis la ligne de commande.'''

# Statistics Module
'''Le module statistiques fournit des fonctions pour les statistiques mathématiques des données numériques. Les fonctions statistiques courantes définies dans ce module sont : moyenne, médiane, mode, écart type, etc.'''
'''from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3'''

# Math Module
'''import math
from math import pi
print(pi)'''

# String Module
'''Un module chaîne est un module utile à plusieurs égards. L'exemple ci-dessous montre quelques utilisations du module chaîne.'''
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Random Module
'''Vous maîtrisez désormais l'importation de modules. Importons-en un autre pour nous familiariser davantage avec cette opération. Importons le module random qui nous donne un nombre aléatoire compris entre 0 et 0,9999... Le module random dispose de nombreuses fonctions, mais dans cette section, nous n'utiliserons que random et randint.'''
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
# random.randint(a, b). Elle génère un entier pseudo-aléatoire compris entre a et b inclusivement.


























