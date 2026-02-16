# EXERCICES LEVEL 1

#1.
'''liste_vide = list()
#2.
Tech = ['HTML', 'CSS', 'JS', 'PYHTON', 'JAVA']
print(Tech)
#3.
print(len(Tech))
#4.
print(Tech[0])
print(Tech[2])
print(Tech[-1])
#5.
infos = ['Lidao', 20, 1.80, 'Single', 'Lomé']
print(infos)
#6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7.
print(it_companies)
#8.
print(len(it_companies))
#9.
first_companies = it_companies[0]
print(first_companies)
middle_companies = it_companies[3]
print(middle_companies)
last_compagnies = it_companies[-1]
print(last_compagnies)
#10.
it_companies[4] = 'MySQL'
print(it_companies)
#11.
it_companies.append('Coursera')
print(it_companies)
#12.
it_companies.insert(4, 'YAS')
print(it_companies)
#13.
it_companies[1] = it_companies[1].upper()
print(it_companies)
#14.
#it_companies = "#; ".join(it_companies)
#print(it_companies)
#15.
does_exist = 'Trootle' in it_companies
print(does_exist)
does_exist = 'GOOGLE' in it_companies
print(does_exist)
#16.
it_companies.sort()
print(it_companies)
#17.
it_companies.reverse()
print(it_companies)
#18.
three_first_companies = it_companies[0:3]
print(three_first_companies)
#19.
last_three_companies = it_companies[-3:]
print(last_three_companies)
#20.
print(len(it_companies))
middle_three_companies = it_companies[3:6]
print(middle_three_companies)
#21.
it_companies.remove(it_companies[0])
print(it_companies)
#22.
it_companies.remove(it_companies[4])
print(it_companies)
#23.
it_companies.remove(it_companies[-1])
print(it_companies)
#24.
it_companies.clear()
print(it_companies)
#25.
del it_companies
print(it_companies)
#26.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
#27.
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)


# EXERCICE LEVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

ages.append(min(ages))
ages.append(max(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
n = len(ages)
if n % 2 == 0:
    # Si le nombre d'éléments est pair, la médiane est la moyenne des deux éléments centraux
    median_age = (ages[n//2] + ages[n//2-1])/2
else:
    median_age = ages[n//2]
print('L\'age médian est : ', median_age)

# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / n
print("L'age moyen est : ", average_age)

# Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print(age_range)

# Compare the value of (min - average) and (max - average), use abs() method
diff_min = abs(min(ages) - average_age)
diff_max = abs(max(ages) - average_age)
print("abs(min - average):", diff_min)
print("abs(max - average):", diff_max)'''

#1.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

n_countries = len(countries)
print(n_countries)
if n_countries % 2 == 0:
    middle_countries = countries[n_countries // 2 - 1: n_countries // 2 + 1]
else:
    middle_countries = [countries[n_countries // 2]]
print("Middle country:", middle_countries)

# 2. Divide countries into two halves
half_index = (n_countries + 1) // 2  # first half gets extra if odd
first_half = countries[:half_index]
second_half = countries[half_index:]
print("First half:", first_half)
print("Second half:", second_half)

# 3. Unpack first three countries and rest as scandic countries
country1, country2, country3, *scandic_countries = countries
print("First three countries:", country1, country2, country3)
print("Scandic countries:", scandic_countries)


