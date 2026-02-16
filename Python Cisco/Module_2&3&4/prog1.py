'''print("2")
print(2)
print("I\'m Monthy Python")
print("I\'m")
print("learning")
print("Python")
print(2+2)
print(9 % 6 % 2)

var = 0  # Assigning 0 to var
print(var == 0)
var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)'''

# Conditions and conditional execution
#EX1
'''number1 = int(input("Entrer la 1ere Valeur : "))
number2 = int(input("Entrer la 2e Valeur : "))
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
print("Le nombre le plus grand est : ", larger_number)'''
#EX2: AUTRE MANIERE
'''number1 = int(input("Entrer la 1ere Valeur : "))
number2 = int(input("Entrer la 2e Valeur : "))
if number1 > number2: larger_number = number1
else: larger_number = number2
print("Le nombre le plus grand est : ", larger_number)'''
#EX3
'''number1 = int(input("Entrer la 1ere Valeur : "))
number2 = int(input("Entrer la 2e Valeur : "))
number3 = int(input("Entrer la 3e Valeur : "))
largest_number = number1
if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3
print("Le nombre le plus grand est : ", largest_number)'''
#EX4 : PLUS SIMPLE
number1 = int(input("Entrer la 1ere Valeur : "))
number2 = int(input("Entrer la 2e Valeur : "))
number3 = int(input("Entrer la 3e Valeur : "))
largest_number = max(number1, number2, number3)
print("Le nombre le plus grand est : ", largest_number)














