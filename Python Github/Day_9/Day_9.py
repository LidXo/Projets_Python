# Exercises: Level 1
#1.
'''age = int(input('Entrer votre age : '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    miss = 18 - age
    print('You need ',miss,' years to learn to drive.')
'''

#2.
'''my_age = int(input('Entrer mon age : '))
your_age = int(input('Entrer votre age : '))
diff_age = abs(your_age - my_age)
if your_age >= my_age:
    print('You are ',diff_age,' years older than me.')
else:
    print('I am ',diff_age,' years older than you.')
'''
#3.
'''a = int(input('Entrer un nombre : '))
b = int(input('Entrer un 2eme nombre : '))
if a > b:
    print(a,' is greater than ',b)
elif a == b:
    print(a,' is equal to ',b)
else:
    print(a,' is less than ',b)'''

# Exercises: Level 2
#1.
'''grade = int(input('Entrer votre note ( sur 100 ) : '))
if 90 <= grade <= 100:
    print('You are grade is A.')
elif 80 <= grade < 90:
    print('You are grade is B.')
elif 70 <= grade < 80:
    print('You are grade is C.')
elif 60 <= grade < 70:
    print('You are grade is D.')
else:
    print('You are grade is F.')'''

#2.
'''print('Janvier, Fevrier, Mars, Avril, Mai, Juin, Juillet, Aout, Septembre, Octobre, Novembre, Decembre')
month = input('Entrer votre mois  : ')
if month == 'Janvier' or month == 'Fevrier' or month == 'Decembre':
    print('The saison is Winter.')
elif month == 'Septembre' or month == 'Octobre' or month == 'Novembre':
    print('The saison is Autumn.')
elif month == 'Avril' or month == 'Mai' or month == 'Juin':
    print('The saison is Spring.')
else:
    print('The saison is Summer.')'''

#3.
'''fruits = ['banana', 'apple', 'mango', 'lemon']
new_fruit = input('Entrer votre fruit : ')
if new_fruit in fruits:
    print('The fruit is already exist in the list.')
else:
    fruits.append(new_fruit)
    print(fruits)'''

# Exercises: Level 3
#1.
# Person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if 'skills' key exists and print the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

# 2. Check if 'Python' is among the skills
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# 3. Determine developer type based on skills
if 'skills' in person:
    skills_set = set(person['skills'])

    if skills_set == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print('He is a fullstack developer')
    else:
        print('unknown title')

# 4. Print married status and country
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


























