# List Comprehension
'''La compréhension de liste en Python est un moyen compact de créer une liste à partir d'une séquence. Il s'agit d'un
moyen rapide de créer une nouvelle liste. La compréhension de liste est considérablement plus rapide que le traitement d'une liste à l'aide d'une boucle « for ».'''
# syntax
# [expression for i in iterable if condition]

# EXAMPLE 1
# one way
'''language = 'Python'
lst = list(language)
print(type(lst))
print(lst)
# second way
lst = [i for i in language] # Crée une liste en itérant sur chaque caractère de la chaîne 'language'
print(type(lst))
print(lst)

# EXAMPLE 2
numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers = [(i, i * i) for i in range(11)]
print(numbers)'''

# EXAMPLE 3
'''even_munbers = [i for i in range(21) if i % 2 == 0]
print(even_munbers)

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list) '''

# Lambda Function
# syntax
'''x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))'''
# EXAMPLE
'''def add_two_nums(a, b):
    return a + b
print(add_two_nums(1, 2))
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(5, 2))


# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22'''

# Lambda Function Inside Another Function
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32



















