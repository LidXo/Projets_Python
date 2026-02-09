"""print('hello world!')
print(100)
print(3.14)"""
from traceback import print_tb

"""20 + 32
5 ** 2
(5 + 9) * (15 - 7)
print(7 +5)"""

"""print(9 / 5)
print(5 / 9)
print(9 // 5)"""

'''print(7.0 / 3.0)
print(7.0 // 3.0) # // affiche l'entier naturel le plus proche
print(7.0 % 3.0)'''  # % affiche le reste de la division

'''print(2 ** 3 ** 2)
print((2 ** 3) ** 2) # c'est une question de priorité
print(16 - 2 * 5 // 3 + 1)'''

# APPEL DE FONCTION
# Carré
'''def square(x):
    return x ** 2
print(square(3))
square(5) # Ne marche pas

# Soustraction
def sub(x, y):
    return x - y
print(sub(9, 6))
print(sub(17, 4))'''

# DATA TYPES
'''print(type("Hello World"))
print(type(17))
print("Hello, World")
print(type(3.2))'''

'''print(type("3.14"))
print(type("17"))
# Tant que les valeurs sont dans '' ou "" ou """""" ou '''''', le type sera toujours STRING
print('''"Oh No", '''she exclaimed''', "Ben's bike is broken" ''')
print("""This message will span
several lines
of the text""") # de cette manière pour revenir à la ligne
print('This is a string')
print("""And so is this.""")'''

'''print(42500)
print(42,500)
print(42, 17, 56, 11, 45, 63)
print(3.4, "Hello", 45)'''

# TYPE CONVERSION FUNCTIONS
'''print(3.14, int(3.14))  # conversion float -> int
print(3.9999, int(3.9999))  # conversion float -> int arrondi à l'entier inférieur
print(3.0, int(3.0))  # conversion float -> int
print(-3.9999, int(-3.9999))  # conversion float -> int arrondi à l'entier inférieur

print("2345", int("2345"))  # conversion string -> int
print(17, int(17))  # conversion int -> int
print(int("23bottles"))'''  # erreur de conversion string -> int

'''print(float("123.45"))  # conversion string -> float
print(type(float("123.45")))  # conversion string -> float

print(str(17)) # conversion int -> string
print(str(123.45)) # conversion float -> string
print(type(str(123.45)))''' # conversion float -> string

# VARIABLES
# EXO1
'''message = "What's up, Doc?"
n = 17
pi = 3.14
print(message)
print(n)
print(pi)
print(type(message))
print(type(n))
print(type(pi))
# EXO2
X = 5
print(X)
X = 10
print(X)'''

# NOM VARIABLES ET MOTS CLÉS
# Réaffectation
'''bruce = 5
print(bruce)
bruce = 7
print(bruce)'''
'''a = 5
b = a
print(a, b) # a = b
a = 3
print(a, b)''' # a ≠ b
# Déclarations et expressions
'''y = 3.14
x = len("Hello") # len affiche la longueur de la chaîne de caractères
print(x, y)
print(2 * len("Hello") + len("Goodbye"))'''

'''def square(x):
    return x ** 2
def sub(x, y):
    return x - y
def add(x, y):
    return x + y'''
'''x = 2
y = 1
print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))'''

'''x = 5
y = 7
print(add(square(x), square(y)))'''

'''print(1+1+(2*3))
print(len("Hello"))

y = 3.14
x = len("Hello")
print(y)
print(x)'''

# Mise à jour des variables
'''x = 6
print(x)
x = x + 1
print(x)'''
# OU
'''x = 6
print(x)
x += 3
print(x)
x -= 1
print(x)'''

# ENTREES UTILISATEUR
'''n = input("Entrer votre nom: ")
print("Bonjour", n)'''

# EXO D'HEURES, MINUTES, SECONDES
'''str_seconds = input("Svp, entrer le nombre de secondes à convertir: ")
total_seconds = int(str_seconds)

hours = total_seconds // 3600 # // affiche l'entier naturel le plus proche
secs_still_remaining = total_seconds % 3600 # % affiche le reste de la division
minutes = secs_still_remaining // 60 # / affiche le résultat en float
secs_finally_remaining = secs_still_remaining % 60

print("hrs=", hours, "min=", minutes, "sec=", secs_finally_remaining)'''

# REPETITION AVEC LA BOUCLE FOR
'''print("Ceci sera exécuter le premier")

for _ in range(3):
    print("Cette ligne sera répétée 3 fois")
    print("Cette ligne aussi")

print("Now")'''

# IMPORTATION DES MODULES
import random

prob = random.random()  # génère un nombre flottant aléatoire dans [0.0, 1.0)
print(prob)  # affiche la valeur générée

# Lancer de dé à 6 faces (1..6). random.randrange(1, 7) exclut 7.
diceTrow = random.randrange(1, 7)  # remarque: 'diceTrow' est probablement une faute; préférer `dice_throw` ou `dice_roll`
print(diceTrow)  # affiche le résultat du lancer












































