# LOOPS (Boucle)
# while ; for

# While Loop
# syntax
'''while condition:
    code goes here'''
# EXAMPLE
'''count = 0
while count < 5:
    print(count)
    count += 1'''

# syntax
'''while condition:
    code goes here
else:
    code goes here'''
# EXAMPLE
'''count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)'''

# Break and Continue - Part 1
# syntax break
'''while condition:
    code goes here
    if another_condition:
        break'''
# EXAMPLE
'''count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break'''

# syntax continue
'''while condition:
    code goes here
    if another_condition:
        continue
'''
# EXAMPLE
'''count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1'''

# For Loop
# syntax
'''for iterator in lst:
    code goes here'''
# EXAMPLE
'''numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)'''
# syntax
'''for iterator in string:
    code goes here'''
# EXAMPLE
'''language = 'Python'
for letter in language:
    print(letter)
    # OR
for i in range(len(language)):
    print(language[i])'''

# Using For loop on tuple
'''# syntax
for iterator in tpl:
    code goes here'''
# EXAMPLE
'''numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)'''

# For loop with dictionary Looping
'''  # syntax
for iterator in dct:
    code goes here'''
# EXAMPLE
'''person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)
for key, value in person.items():
    print(key, value)'''

# Using For Loop in set
'''# syntax
for iterator in st:
    code goes here'''
'''it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)'''

# Break and Continue - Part 2
'''# syntax break
for iterator in sequence:
    code goes here
    if condition:
        break'''
# EXAMPLE
'''numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break'''

'''  # syntax continue
for iterator in sequence:
    code goes here
    if condition:
        continue'''
# EXAMPLE
'''numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    if number != 5:
        print('Next number should be ', number + 1)
    print('outside the loop')'''

# The Range Function
'''lst = list(range(11))
print(lst)
st = set(range(1, 11))
print(st)

lst = list(range(0, 11, 2))
print(lst) # Affiche les nbres paires
st = set(range(1, 11, 2))
print(st) # Affiche les nbres impairs

lst = list(range(11, 0, -2))
print(lst)'''

'''# syntax
for iterator in range(start, end, step):'''

# Nested For Loop
'''# syntax
for x in y:
    for t in x:
        print(t)'''
# EXAMPLE
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# For Else
'''# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')'''
# EXAMPLE
for number in range(11):
    print(number)
else:
    print('La boucle s\'arrete à : ', number)

# Pass
for number in range(6):
    pass






















