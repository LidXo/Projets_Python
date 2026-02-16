# EXERCICES LEVEL 1
#1.
'''empty_tuple = tuple() # OR
empty_tuple1 = ()
#2.
names = ('Lidao', 'Ewazam', 'Biguedinam', 'David')
print(names)
#3.
brothers = ('Lidao', 'Ewazam')
sisters = ('Biguedinam', 'Essowereou')
siblings = brothers + sisters
print(siblings)
#4.
print(len(siblings))
#5.
family_members = list(siblings)
family_members.append('Dad')
family_members.append('Mom')
print(family_members)


# EXERCICES LEVEL 2
#1.
sibling1, sibling2, sibling3, sibling4, *parents = family_members
print("Siblings: ", sibling1, sibling2, sibling3, sibling4)
print("Les Parents : ", parents)'''
#2.
fruits = ('apple', 'banana', 'orange', 'mango')
vegetables = ('Tomato', 'Ail', 'Oignon', 'Poivre')
food_stuff_tp = fruits + vegetables
print(food_stuff_tp)
#3.
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
#4.
n = len(food_stuff_tp)
middle_items = food_stuff_tp[n//2 - 1 : n//2 + 1]
print("Middle items (tuple):", middle_items)
n = len(food_stuff_lt)
middle_items = food_stuff_lt[n//2 - 1 : n//2 + 1]
print("Middle items (list):", middle_items)
#5.
first_three_items = food_stuff_lt[:3]
print("First three items :", first_three_items)
last_three_items = food_stuff_lt[-3:]
print("Last three items :", last_three_items)
#6.
del food_stuff_tp
#7.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)














