# DAY_11
import math
# Exercises: Level 1
#1.
'''def add_two_numbers(x, y):
    return x + y
print(add_two_numbers(1, 2))
#2.
def area_of_circle(r):
    area = math.pi * r ** 2
    return area
print(area_of_circle(3))
#3.
def add_all_nums(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return ("Error")
        total += arg
    return total
print(add_all_nums(1, 2, 3, 10))
#4.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
print(convert_celsius_to_fahrenheit(32))'''
# 5.
'''def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "Mois invalide."
print(check_season('october'))'''
#6.
'''def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Division par zero"
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 4))'''
#7.
'''def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "Ce n'est pas une équation du deuxieme dégré"

    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Pas de solution"
print(solve_quadratic_eqn(1, 1, 1))'''
#8.
'''def print_list(lst):
    if item in lst:
        print(item)
print(print_list([1, 2, 3]))'''

#9.
'''def reverse_list(arr):
    # Initialise une liste vide pour stocker les éléments inversés
    reversed_arr = []
    # Parcourt la liste d'origine en partant du dernier index jusqu'à 0
    for i in range(len(arr) - 1, -1, -1):
        # Ajoute l'élément actuel à la nouvelle liste
        reversed_arr.append(arr[i])
    # Retourne la liste inversée
    return reversed_arr
print(reverse_list([1, 2, 3]))'''

#10.
'''def capitalize_list_items(lst):
    # Initialise une liste vide pour stocker les éléments transformés
    capitalized = []
    # Parcourt chaque élément de la liste fournie en argument
    for item in lst:
        # Vérifie si l'élément actuel est une chaîne de caractères
        if isinstance(item, str):
            # Met la première lettre en majuscule et l'ajoute à la nouvelle liste
            capitalized.append(item.capitalize())
        else:
            # Si ce n'est pas une chaîne, ajoute l'élément tel quel
            capitalized.append(item)
    # Retourne la nouvelle liste contenant les éléments traités
    return capitalized
print(capitalize_list_items(['lidao', 'trader millionnaire']))'''

#11.
'''def add_list(lst, item):
    lst.append(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_list(food_stuff, 'Meat'))
numbers = [2, 3, 7, 9];
print(add_list(numbers, 5))'''

#12.
'''def remove_item(list, item):
    if item in list:
        list.remove(item)
        return list
    
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))'''

#13.
'''def sum_of_numbers(num):
    total = 0
    for i in range(num):
        total += i
    return total
print(sum_of_numbers(15))'''

#14.
'''def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total
print(sum_of_odds(10))

#15.
def sum_of_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_even(10))'''


# Exercises: Level 2
#1.
import math
from collections import Counter

'''def evens_and_odds(n):
    if not isinstance(n, int) or n < 0:
        return "Error"
    evens = 0
    odds = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens += i
        else:
            odds += i
print(evens_and_odds(10))'''

#2.
























