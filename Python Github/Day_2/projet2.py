# DAY 1
'''print("Hello world !")

print(2 + 3)
print(4 - 3)
print(8 * 7)
print(9 / 8)
print(9 % 8)
print(3 ** 2)
print(17 // 3) # Affiche la partie entière
print(17 % 3) # Reste'''

# Type de données
'''print(type(10))
print(type(3.14))
print(type(1 + 3j)) #Complexe
print(type('Lidao'))
print(type([1, 2, 3])) #list
print(type({'name': 'Lidao'})) #dictionnaire
print(type({9.8, 3.14, 2.7}))''' # Set (Ensemble de nbres flottants)


# DAY 2
# Variables en Python
'''first_name = 'Lidao'
last_name = 'ABIYI'
country = 'Togo'
city = 'Lomé'
age = 20
is_married = True
Skills = ['Python','HTML','JS','CSS']
person_info = {
    'firstname': 'Lidao',
    'lastname': 'ABIYI',
    'country': 'Togo',
    'city': 'Lomé'
}
# Afficher les valeurs
print('Nom: ',last_name)
print('le nombre de caractères dans le nom: ', len(last_name))
print('Prenom: ',first_name)
print('Le nombre de caractères dans le prénom: ', len(first_name)) # len affiche le nbre de caractères
print('Pays: ', country)
print('Ville: ', city)
print('Age: ', age)
print('Marié: ', is_married)
print('Compétences: ', Skills)
print('Infos Personnelles: ', person_info)'''

# Déclarer +ieurs variables sur une seule ligne
'''nom, prenom, pays, age, is_married = 'ABIYI', 'Lidao', 'Togo', 20, True

print(nom, prenom, pays, age, is_married)
print('Nom: ', nom)
print('Prenom: ', prenom)
print('Pays: ', pays)
print('Age: ', age)
print('Marié ? : ', is_married)'''

# Entrée User
'''first_name = input('Entrer votre nom: ')
age = int(input('Entrer votre age: '))
print('Votre nom est: ', first_name)
print('Et votre age est: ', age)'''
# Convertion
# int to float
'''num_int = 10
print('num_int: ', num_int )
num_float = float(num_int)
print ('num_float: ', num_float)'''
# float to int
'''num_float = 3.14
print('num_float: ', num_float)
num_int = int(num_float)
print('num_int: ', num_int)'''
# int to str
'''num_int = 10
print('num_int : ', num_int)
num_str = str(num_int)
print(num_str)'''
# str to int or float
'''num_str = '10.6'
num_float = float(num_str) # 1er Convertit cc en dec
num_int = int(num_float) # 2eme convertit dec en int
print('num_int: ', int(num_str))
print('num_float: ', float(num_str))
num_int = int(num_float)
print('num_int: ', int(num_int))'''
# str to list
nom = 'ABIYI'
print(nom)
nom_to_list = list(nom)
print(nom_to_list)



# DAY 3




