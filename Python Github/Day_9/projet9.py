# CONDITIONALS

# if condition
# syntax
'''if condition:
    this part of code runs for truthy conditions'''
# EXAMPLE 1
a = 3
if a > 0:
    print('A is positive')

# if else
# syntax
'''if condition:
    this part of code runs for truthy conditions
else:
    this part of code runs for false conditions'''
# EXAMPLE
a = 3
if a < 0:
    print('A est négative')
else:
    print('A est positive')

# if elif else
# syntax
'''if condition:
    code
elif condition:
    code
else:
    code'''
# EXAMPLE
a = 0
if a > 0:
    print('A est positive')
elif a < 0:
    print('A est negative')
else:
    print('A est Zéro')

# plus bref, plus Courte
# syntax
# code if condition else code
# EXAMPLE
a = 3
print('A est positive') if a > 0 else print('A est negative')

# Conditions imbriquées
# syntax
'''if condition:
    code
    if condition:
        code'''
# EXAMPLE
a = 20
if a > 0:
    if a % 2 == 0:
        print('A est positive et pair')
    else:
        print('A est positive et impair')
elif a == 0:
    print('A is Zero')
else:
    print('A is negative')

# If Condition and Logical Operators
# syntax
'''if condition and condition:
    code'''
# EXEMPLE
a = 0
if a > 0 and a % 2 == 0:
    print('A est positive et pair')
elif a > 0 and a % 2 != 0:
    print('A est positive et impair')
elif a == 0:
    print('A is Zero')
else:
    print('A is negative')

# if and Or Logical Operators
# syntax
'''if condition or condition:
    code'''
# EXAMPLE
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied')


























