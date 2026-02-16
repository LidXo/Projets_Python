# SETS ( ENSEMBLES )

# creation
empty_st = set()
# with values
st = {'item1', 'item2', 'item3', 'item4'}

# EXAMPLE
fruits = {'banana', 'apple', 'mango', 'lemon'}
# Getting Set's Length
'''print(fruits)
print(len(fruits))

# Accessing Items in a Set
# Vérification d'un élément
print("Does set st contain item3 ? : ", 'item3' in st)
print('mango' in fruits)'''

# Adding Items to a Set
# add()
'''st.add('item5')
print(st)
fruits.add('orange')
print(fruits)
# Add multiple items using update()
st.update(['item5', 'item6', 'item7'])
print(st)
vegetables = {'tomato', 'patate', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)
# Removing Items from a Set
st.remove('item7')
print(st)
# pop() methods
fruits.pop()
print(fruits)

# Clearing Items in a Set
st.clear()
print(st)
fruits.clear()
print(fruits)

# Deleting a Set
# syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# del st

# Converting List to Set
lst = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']
st = set(lst)
print(st)

# Joining Sets
# syntax union()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2
print(st3)
# syntax update()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1

# Finding Intersection Items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item2', 'item3'}
st1.intersection(st2)
print(st1.intersection(st2))
# EXAMPLE
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)# {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
print(python.intersection(dragon)) # python & dragon

# Checking Subset and Super Set Vérification du sous-ensemble et du sur-ensemble
# Subset: issubset()
# Super set: issuperset()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1))
print(st1.issuperset(st2))'''
# EXAMPLE
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))     # False

# Checking the Difference Between Two Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set() : st2 - st1
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2  : st2 - st1
# EXAMPLE
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python

# Finding Symmetric Difference Between Two Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1

# EXEMPLE
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon

# Joining Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
# EXAMPLE
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}




















