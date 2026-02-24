# DICTINNAIRES
# CREATION
empty_dict = {}
dct = {'Key1':'value1', 'Key2':'value2', 'Key3':'value3'}
# EXAMPLE
person = {
    'first_name' : 'Lidao',
    'last_name' : 'ABIYI',
    'age' : 20,
    'country' : 'Togo',
    'is_married' : True,
    'skills' : ['JavaScript', 'React', 'Python'],
    'address' : {
        'street' : 'Street',
        'zipcode' : '04653'
    }
}
print(dct)
print(person)

# Dict Length
print(len(dct))
print(len(person))

# Accessing Dictionary Items
print(dct['Key1'])
print(dct['Key3'])
# EXAMPLE
print(person['first_name'])
print(person['country'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['street'])
# L'accès à un élément par son nom de clé génère une erreur si la clé n'existe pas. Pour éviter cette erreur, nous devons d'abord vérifier si une clé existe ou nous pouvons utiliser la méthode get. La méthode get renvoie None, qui est un type de données d'objet NoneType, si la clé n'existe pas.
print(person.get('last_name'))
print(person.get('age'))
print(person.get('is_married'))

# Adding Items to a Dictionary
dct['Key4'] = 'value4'
print(dct)

person['job_title'] = 'Data Engineer'
person['skills'].append('Github')
print(person)

# Modifying Items in a Dictionary
dct['Key1'] = 'value-one'
print(dct)

person['first_name'] = 'LidXo'
person['age'] = 21
print(person)

# Vérification des clés dans un dictionnaire
print('Key2' in dct)
print('Key3' in dct)

# Suppression de paires clé-valeur d'un dictionnaire
dct.pop('Key4')
dct.popitem()
del dct['Key2']
print(dct)
# EXEMPLE
person.pop('first_name')
person.popitem()
del person['is_married']
print(person)

# Changing Dictionary to a List of Items
'''print(dct.items())

# Clearing a Dictionary
print(dct.clear())

# Deleting a Dictionary
del dct'''

# Copy a Dictionary
dct_copy = dct.copy()

# Getting Dictionary Keys as a List
keys = dct.keys()
print(keys)

 # Getting Dictionary Values as a List

values = dct.values()
print(values)






















