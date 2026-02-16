# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

'''
# EXERCICES LEVEL 1
#1.
print(len(it_companies))
#2.
it_companies.add('Twitter')
print(it_companies)
#3.
it_companies.update({'Tesla', 'Porsche', 'Lambo'})
print(it_companies)
#4.
it_companies.remove('Tesla')
print(it_companies)
#5.


'''
'''
# EXERCICES LEVEL 2
#1.
print(A.union(B))
#2.
print(A.intersection(B))
#3.
print(A.issubset(B))
#4.
print(A.isdisjoint(B))
#5.
print(A.union(B))
print(B.union(A))
#6.
print(A.symmetric_difference(B))
#7.
del A
del B'''

# EXERCICE 3
#1.
age_set = set(age)
print(len(age_set))
print(len(age))
#2.
'''String → texte immuable

List → collection ordonnée modifiable

Tuple → collection ordonnée non modifiable

Set → collection non ordonnée sans doublons'''
#3.
sentence = "I am a teacher and I love to inspire and teach people"

words = sentence.split()
unique_words = set(words)

print(len(unique_words))
print(unique_words)













