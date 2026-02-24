# DAY 13
#1.
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [n for n in numbers if n <= 0]
print(negatives_and_zero)
#2.
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in list_of_lists for item in sublist]
print(flattened)
#3.
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuple_list)
#4.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [[c[0].upper(), c[0][:3].upper(), c[1].upper()] for sublist in countries for c in sublist]
print(flattened_countries)
# [['FINLAND','FIN','HELSINKI'], ['SWEDEN','SWE','STOCKHOLM'], ['NORWAY','NOR','OSLO']]
#5.
country_dicts = [{'country': c[0].upper(), 'city': c[1].upper()} for sublist in countries for c in sublist]
print(country_dicts)
# [{'country':'FINLAND','city':'HELSINKI'}, ...]
#6.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{first} {last}" for sublist in names for (first, last) in sublist]
print(concatenated_names)
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#7.
# Slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')

# Intercept
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

print("Slope:", slope(1, 2, 3, 6))        # 2.0
print("Y-intercept:", y_intercept(1, 2, 3, 6))  # 0.0






















