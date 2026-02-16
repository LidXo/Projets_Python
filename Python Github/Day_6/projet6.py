# DAY 6
# TUPLES

# Creation d'un tuple
# syntax
tuple_vide = ()
# ou
tuple_vide1 = tuple()
#AVEC LES VALEURS
tpl = ('item1', 'item2', 'item3')
fruits = ('banane', 'orange', 'mangue', 'melon')
print(fruits)
# longueur du Tuple
'''print(len(fruits))
# Accès aux éléments d'un tuple
# Positive indexing
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[-1]
print(last_fruit)
# Negative indexing
first_fruit = fruits[-4]
print(first_fruit)
second_fruit = fruits[-3]
print(second_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# Découpage de tuples
# Plage des indices positifs
all_fruits = fruits[0:4] # OR
# all_fruits = fruits[0:]
print(all_fruits)
# Plage des indices negatifs
all_fruits = fruits[-4:]
print(all_fruits)
middle_fruit = fruits[-3:-1]
print(middle_fruit)
orange_reste = fruits[-3:]
print(orange_reste)'''

# Convertir des tuples en listes
# syntax
'''tpl = ('item1', 'item2', 'item3')
lst = list(tpl)
# EXEMPLE
liste_fruits = list(fruits)
print(liste_fruits)
liste_fruits[0] = 'apple'
print(liste_fruits)
liste_fruits = tuple(liste_fruits)
print(liste_fruits)

#Vérification d'un élément dans un tuple
print('orange' in fruits)
print('apple' in fruits)
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
print(fruits)'''

# Joindre des tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
# EXEMPLE
legumes = ('Tomate', 'Patate', 'Cabbage','Onion', 'Carrot')
fruits_legumes = fruits + legumes
print(fruits_legumes)

# Deleting Tuples
tpl1 = ('item1', 'item2', 'item3')
del tpl1
























