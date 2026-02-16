# CREATION D'UNE LISTE
liste = list()

liste_vide = list() # une liste vide
print(len(liste_vide)) # 0
# OU
liste_vide1 = [] # liste vide
print(len(liste_vide1)) # 0

#EXEMPLE
fruits = ['banane', 'avocat', 'mangue', 'melon']
legumes = ['tomate', 'patate', 'carrote', 'ail']
produit_animal = ['lait', 'viande', 'beurre', 'yaourt']
web_tech = ['HTML', 'CSS', 'JS', 'REACT', 'JAVA', 'PYTHON', 'MySQL']
pays = ['Togo', 'Dubai', 'Ghana', 'France', 'USA', 'Canada']

print('Fruits: ', fruits)
print('Nombre de Fruits: ', len(fruits))
print('Légumes: ', legumes)
print('Nombre de légumes: ', len(legumes))
print('Produits: ', produit_animal)
print('Nombre de Produits: ', len(produit_animal))
print('Web technologies: ', web_tech)
print('Nombre de Web Technologies: ', len(web_tech))
print('Pays: ', pays)
print('Nombre de Pays: ', len(pays))
# Les listes peuvent contenir des éléments de différents types de données.
lst = ['Lidao', 20, True, {'pays':'Togo', 'city':'Lomé'}]
print(lst)

# Accès aux éléments d'une liste à l'aide d'un index positif
fruits = ['banane', 'avocat', 'mangue', 'melon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
third_fruit = fruits[2]
print(third_fruit)
last_fruit = fruits[-1]
print(last_fruit)

#Accès aux éléments d'une liste à l'aide de l'indexation négative
fruits = ['banane', 'avocat', 'mangue', 'melon']
first_fruit = fruits[-4]
print(first_fruit)
second_fruit = fruits[-3]
print(second_fruit)
third_fruit = fruits[-2]
print(third_fruit)
last_fruit = fruits[-1]
print(last_fruit)

#Liste des articles à déballer
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
# Déballage de la liste : les 3 premiers éléments vont dans des variables distinctes, le reste dans une liste 'rest'
# Ici, Python utilise l’unpacking (déballage) des listes avec l’opérateur *.
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)
# EXEMPLE 1
fruits = ['banane', 'avocat', 'mangue', 'melon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)
# EXEMPLE 2
first, *rest, second, third, ten = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(rest)
print(second)
print(third)
print(ten)
# EXEMPLE 3
pays = ['Allemagne', 'FRANCE', 'USA', 'SUEDE', 'DANEMARK', 'TOGO', 'GHANA', 'COTE D\'IVOIRE', 'MAROC', 'SENEGAL', 'ARABS UNIS']
gr, fr, usa, sw, *rest, gh = pays
print(gr)
print(fr)
print(usa)
print(sw)
print(rest)
print(gh)

# Découpage d'éléments d'une liste
# Positive Indexing
fruits = ['banane', 'avocat', 'mangue', 'melon']
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits1 = fruits[0:] # Autre manière
print(all_fruits1)
avocat_et_mangue = fruits[1:3]
print(avocat_et_mangue)
avocat_mangue_melon = fruits[1:4]
print(avocat_mangue_melon)
avocat_melon = fruits[::2]
print(avocat_melon)
# Negative Indexing
fruits = ['banane', 'orange', 'mangue', 'melon']
all_fruits = fruits[-4:]
print(all_fruits)
orange_mangue = fruits[-3:-1]
print(orange_mangue)
banane_mangue = fruits[::2]
print(banane_mangue)
orange_mangue_melon = fruits[-3:]
print(orange_mangue_melon)
reverse_fruits = fruits[::1]
print(reverse_fruits)

# Modification des listes
fruits = ['banane', 'orange', 'mangue', 'melon']
print(fruits)
fruits[0] = 'avocat'
print(fruits)
fruits[1] = 'apple'
print(fruits)
fruits[-1] = 'lime'
print(fruits)

# Vérification des éléments d'une liste (does_exist)
fruits = ['banane', 'orange', 'mangue', 'melon']
does_exist = 'banane' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

#  Ajouter des éléments à une liste (append)
#lst = list()
#lst.append(item)
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

# Insérer des éléments dans une liste (insert ajoute un élément à une posiition précise et décalle le autres éléments)
#lst = ['item1', 'item2']
#lst.insert(index, item)
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(1, 'lime')
print(fruits)

# SUPPRIMER Items from a List
# syntax
#lst = ['item1', 'item2']
#lst.remove(item)
#EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon', 'banana', 'mango']
print(fruits)
fruits.remove('banana')
print(fruits)
fruits.remove('mango')
print(fruits)

# Suppression d'éléments à l'aide de Pop
#lst = ['item1', 'item2']
#lst.pop()
#lst.pop(index)
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
print(fruits)
fruits.pop() # last item
print(fruits)
fruits.pop(0)
print(fruits)

# Removing Items Using Del
# syntax
# lst = ['item1', 'item2']
#del lst[index] # only a single item
#del lst        # to delete the list completely
fruits = ['banane', 'orange', 'mangue', 'melon']
print(fruits)
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
fruits = ['banane', 'orange', 'mangue', 'melon']
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
print(fruits)

# Effacer les éléments de la liste (clear)
# syntax
#lst = ['item1', 'item2']
#lst.clear()
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
fruits.clear()
print(fruits)

# Copier une liste (copy)
# syntax
#lst = ['item1', 'item2']
#lst_copy = lst.copy()
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
fruits_copie = fruits.copy()
print(fruits_copie)

# Joining Lists
# Plus Operator (+)
#list3 = list1 + list2
# EXEMPLE
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banane', 'orange', 'mangue', 'melon']
legumes = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_et_legumes = fruits + legumes
print(fruits_et_legumes)

# with extend()
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
# EXEMPLE
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6, 7]
num1.extend(num2)
print('Nombres: ', num1)
# EXEMPLE 2
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Entiers: ', negative_numbers)
fruits = ['banane', 'orange', 'mangue', 'melon']
legumes = ['Tomato', 'Potato', 'Cabbage', 'Onion']
fruits.extend(legumes)
print('Fruits et légumes: ', fruits)

# Compter les éléments d'une liste ( count() )
# syntax
# lst = ['item1', 'item2']
# lst.count(item)
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
print(fruits.count('banane'))
ages = [22, 19, 34, 13, 22, 22, 5, 6]
print(ages.count(22))

# Recherche de l'index d'un élément index()
# syntax
#lst = ['item1', 'item2']
#lst.index(item)
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
print(fruits.index('mangue'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(19)) # index indique la position

# Reversing a List reserve()
# syntax
#lst = ['item1', 'item2']
#lst.reverse()
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# Trier les éléments de la liste sort()
# syntax
# lst = ['item1', 'item2']
# lst.sort()                # ascending
# lst.sort(reverse=True)    # descending
# EXEMPLE
fruits = ['banane', 'orange', 'mangue', 'melon']
fruits.sort() # ORDRE
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 25]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

# Sorted()
fruits = ['banane', 'orange', 'mangue', 'melon']
print(sorted(fruits))
fruits = ['banane', 'orange', 'mangue', 'melon']
fruits = sorted(fruits, reverse=True)
print(fruits)





























