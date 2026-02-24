# Functions
# CREATION avec le mot clé def
'''def

# DECLARATION DE FONCTION
def function_name():
    codes
    codes
# APPEL DE FONCTION
function_name()'''

# FUNCTION SANS PARAMETRES
# EXEMPLE
'''def generate_full_name():
    first_name = 'Lidao'
    last_name = 'ABIYI'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name() # Appel de la fonction

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# Function Returning a Value - Part 1
def generate_full_name():
    first_name = 'Lidao'
    last_name = 'ABIYI'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())'''

# Function with Parameters
# syntax
# declarer une fonction
'''def function_name(parameter):
    codes
    codes
# calling function
print(function_name(argument))'''

# EXEMPLE ( un seul parametre )
'''def greetings (name):
    message = name + ', Welcome to Python For Everyone!'
    return message
print(greetings('Lidao'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x ** 2
print(square_number(5))

import math

def area_of_circle(r):
    area = math.pi * r**2
    return area
print(area_of_circle(5))

def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_of_numbers(20))'''

# EXEMPLE ( Avec 2 parametres )
# syntax
'''def function_name(param1, param2):
    codes
    codes
print(function_name(arg1, arg2))'''

'''def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Je m\'appelle : ', generate_full_name('Lidao', 'ABIYI'))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Somme des deux nombres est : ', sum_two_numbers(5, 6))

def calculate_age(current_year, previous_year):
    age = current_year - previous_year
    return age
print('J\'ai ', calculate_age(2026, 1923), 'ans.')

def weight_of_object(mass, garvity):
    weight = str(mass * garvity) + ' N'
    return weight
print('Le poids est : ', weight_of_object(30, 9.8))'''

# Transmission d'arguments avec mot clé et valeur
# syntax
# Declaring a function
'''def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe'))'''
# EXAMPLE
'''def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
print_fullname(first_name = 'Lidao', last_name = 'ABIYI')

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num1 = 9, num2 = 2))'''

# Function Returning a Value - Part 2
# Returning a string
'''def print_name(firstname):
    return firstname
print(print_name('Lidao'))

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print(print_full_name(firstname = 'Lidao', lastname = 'ABIYI'))

# Returning a number
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(9, 2))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('J\'ai ', calculate_age(2026, 2005), 'ans.')

# Returning a boolean
def is_even(n):
    if n % 2 == 0:
        return True
    return False
print(is_even(10))
print(is_even(19))'''

# Returning a list
'''def find_even_numbers(n):
    evens = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
print(find_even_numbers(19))'''

# Function with Default Parameters
'''# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)'''
# EXAMPLE
'''def greetings (name = 'Lidao'):
    message = name + ', Welcome to Python For Everyone!'
    return message
print(greetings())
print(greetings('David'))

def generate_full_name(first_name = 'Lidao', last_name = 'ABIYI'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('David', 'SMITH'))

def calculate_age(birth_year, current_year = 2021):
    age = current_year - birth_year
    return age
print('Age : ', calculate_age(1923))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))'''

# Nombre arbitraire d'arguments
'''# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)'''
# EXAMPLE
'''def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(1, 2, 3, 4))
print(sum_all_nums(1, 2, 3, 4, 34, 21))

# Nombre de paramètres par défaut et arbitraire dans les fonctions
def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team1', 'ABIYI', 'Book', 'David')'''

# Décompression du dictionnaire
'''def greet(name, location):
    print('Hi there', name, "how is the weather in", location)

greet(name = 'Lidao', location = 'Dubai')

my_dict = {"name": "Lidao", "location": "Dubai"}
greet(**my_dict)'''
# L'opérateur ** décompresse le dictionnaire, en transmettant ses paires clé-valeur comme arguments clés à la fonction.

# Nombre arbitraire d'arguments nommés
'''def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)'''

# Function as a Parameter of Another Function*
def square_number(n):
    return n**n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))
print(do_something(square_number, 4))






































