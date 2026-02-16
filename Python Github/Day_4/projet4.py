# STRING
'''letter = 'P'
print(letter)
print(len(letter))
greeting = 'Hello World!'
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

multiline_string = ''I am a teacher and enjoy teaching.
        I didn't find anything as rewarding as empowering people.
        That is why I created 30 days of Python'''
'''print(multiline_string)

multiline_string2 = """I am a teacher and enjoy teaching.
        I didn't find anything as rewarding as empowering people.
        That is why I created 30 days of Python"""
print(multiline_string2)'''

# STRING CONCATENATION

'''first_name = 'Lidao'
last_name = 'ABIYI'
space = ' '
full_name = first_name + space + last_name
print(full_name)

print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))'''

# ESCAPE SEQUENCES IN STRING ( \n: new line, \t: Tab means(8 spaces)
#\\: Back slash, \': Single quote ('), \": Double quote ("))

'''print('I hope everyone is enjoying the python Challenge.\nAre you ?') # \n retour à la ligne
print('Days\tTopics\tExercices') # \t donne de l'espace en 2 mots
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t7\t30')
print('Day 4\t8\t40')
print('This is a backslash symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')'''

#STRING FORMATING
# String seulement
'''first_name = 'Lidao'
last_name = 'ABIYI'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)'''

# STRING AND NUMBERS
'''radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formed_string = 'The following are Python libraries : %s' %python_libraries
print(formed_string)'''

# AURES FORMATS
'''first_name = 'Lidao'
last_name = 'ABIYI'
language = 'Python'
formed_string = 'I am {} {}. I teach {}' .format(first_name, last_name, language)
print(formed_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} ** {} = {}'.format(a, b, a ** b))'''

'''radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formated_string)

# f-string
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')'''

# Séquences de Personnage
'''language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)'''

# ACCES AU CARACTERES DU STRING
'''language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
last_letter1 = language[-1]
print(last_letter1)
second_last = language[-2]
print(second_last)'''

# Trancher les strings
'''language = 'Python'
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)

last_three1 = language[-3:]
print(last_three1)
last_three2 = language[3:]
print(last_three2)'''

# Inverser un string
'''greeting = 'Hello World !'
print(greeting[::-1]) # [::-1] pour renverser

# Sauter des caractères de string

language = 'Python'
pto = language[0:6:2]
print(pto)'''

# Méthodes de String
# capitalize(): Converts the first character of the string to capital letter
'''challenge = 'thirty days of Python'
print(challenge.capitalize())
# count(): renvoie le nombre d'occurrences d'une sous-chaîne dans une chaîne, count(sous-chaîne, début=.., fin=..). Le début correspond à l'index de départ du comptage et la fin correspond à l'index de fin du comptage.
challenge = 'thirty days of Python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))'''
# endswith():  vérifie si une chaîne se termine par une fin spécifique.
'''challenge = 'thirty days of Python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))
# expandtabs(): Remplace le caractère de tabulation par des espaces, la taille de tabulation par défaut est 8. Il prend en compte l'argument de taille de tabulation.
challenge = 'thirty\tdays\tof\tPython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))'''
# find(): Renvoie l'index de la première occurrence d'une sous-chaîne. Si aucune occurrence n'est trouvée, renvoie -1.
'''challenge = 'thirty days of Python'
print(challenge.find('y'))
print(challenge.find('th'))
# rfind(): Renvoie l'index de la dernière occurrence d'une sous-chaîne. Si aucune occurrence n'est trouvée, renvoie -1
challenge = 'thirty days of Python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))'''
# format(): formate la chaîne pour obtenir un résultat plus agréable
'''first_name = 'Lidao'
last_name = 'ABIYI'
age = 20
job = 'Student'
country = 'Togo'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence)'''
# index(): Renvoie l'index le plus bas d'une sous-chaîne. Les arguments supplémentaires indiquent l'index de début et de fin (par défaut 0 et longueur de la chaîne - 1). Si la sous-chaîne n'est pas trouvée, une erreur valueError est levée.
'''challenge = 'thirty days of Python'
sub_string = 'da'
print(challenge.index(sub_string))
print(challenge.index(sub_string, 9))'''
# rindex(): Renvoie l'index le plus élevé d'une sous-chaîne. Les arguments supplémentaires indiquent l'index de début et de fin (par défaut 0 et longueur de la chaîne - 1).
'''challenge = 'thirty days of Python'
sub_string = 'da'
print(challenge.rindex(sub_string))
# print(challenge.rindex(sub_string, 9))
print(challenge.rindex('on', 8))'''
# isalnum(): Vérifie les caractères alphanumériques
'''challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
challenge = '30DaysPython'
print(challenge.isalnum())
challenge = 'Thirty Days Python'
print(challenge.isalnum())''' # Les espaces ne sont âs des alphanum
# isalpha(): Vérifie si tous les éléments de la chaîne sont des caractères alphabétiques (a-z et A-Z)
'''challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha()) '''     # False
# isdecimal():  Vérifie si tous les caractères d'une chaîne sont des chiffres décimaux (0-9).
'''challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
# isdigit(): Vérifie si tous les caractères d'une chaîne sont des chiffres (0-9 et certains autres caractères Unicode représentant des chiffres).
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())''' # True

# join(): Renvoie une chaîne concaténée.
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

#strip()
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
# replace()
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
#
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
#
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
#
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
#
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False









