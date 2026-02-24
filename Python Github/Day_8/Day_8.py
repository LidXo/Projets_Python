# Exercises: Day 8

#1. Create an empty dictionary called dog
#   dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Pitou', 'color':'white', 'breed':'Berger Allemand', 'legs':4, 'age':3}
print(dog)
#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'John',
    'last_name':'Doe',
    'gender':'Male',
    'age':25,
    'marital_status':'Married',
    'skills':['Python', 'Java', 'Ruby'],
    'country':'France',
    'city':'Paris',
    'address':'Sada'
}
print(student)

#4. Get the length of the student dictionary
print(len(student))

#5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
type_skills = type(skills)
print(type_skills)

#6. Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')
print(student)

#7. Get the dictionary keys as a list
keys = list(student.keys())
print(keys)

#8. Get the dictionary values as a list
values = list(student.values())
print(values)

#9. Change the dictionary to a list of tuples using items() method
tple = list(student.items())
print(tple)

#10. Delete one of the items in the dictionary
student.pop('first_name')
print(student)

#11. Delete one of the dictionaries
del student























