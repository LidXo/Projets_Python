#1.
mot1 = 'Thirty'
mot2 = 'Days'
mot3 = 'Of'
mot4 = 'Python'
space = ' '
sentence = mot1 + space + mot2 + space + mot3 + space + mot4
print(sentence)
#2.
mot5 = 'Coding'
mot6 = 'For'
mot7 = 'All'
space1 = ' '
sentence1 = mot5 + space1 + mot6 + space1 + mot7
#print(sentence1)
#3.
Company = sentence1
#4.
#print(Company)
#5.
print(len(Company))
#6.
print(Company.upper())
#7.
print(Company.lower())
#8.
print(Company.title())
print(Company.capitalize())
print(Company.swapcase())
#9. Cut(slice) out the first word of Coding For All string.
first_word = Company[:6]
print(first_word)
#10.
print(Company.find("Coding"))
print(Company.index("Coding"))
print("Coding" in Company)
#11.
print(Company.replace("Coding", "Python"))
#12.
text = "Python For Everyone"
print(text)
new_text = text.replace("Everyone", "All")
print(new_text)
#13.
print(Company)
print(Company.split(" "))
#14.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
result = companies.split(",")
print(result)
#15.
print(Company[0])
#16.
print(Company[-1])
#17.
print(Company[11])
#18.
text = 'Python For Everyone'
acronym = "".join(word[0] for word in text.split())
# word[0] signifie : prendre la première lettre de chaque mot
# text.split() découpe la phrase en une liste de mots
# (word[0] for word in text.split()) est une expression génératrice
# qui parcourt chaque mot et récupère sa première lettre :
# "P", "F", "E
print(acronym)
#19.
text1= 'Coding For All'
acronym1 = "".join(word[0] for word in text1.split())
print(acronym1)
#20. Position of first 'C' in "Coding For All"
text = "Coding For All"
print(text.index("C"))
#21. Position of first 'F' in "Coding For All"
text = "Coding For All"
print(text.index("F"))
#22. Position of last 'l' in "Coding For All People"
text = "Coding For All People"
print(text.rfind("l"))
#23. First occurrence of 'because'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
#24. Last occurrence of 'because'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex("because"))
#25. Slice out 'because because because'
sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.find("because")
end = sentence.rindex("because") + len("because")
print(sentence[start:end])
#26. First occurrence of 'because' (again)
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
#27. Slice out 'because because because' (again)
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[31:54])
#28. Does 'Coding For All' start with 'Coding'?
text = "Coding For All"
print(text.startswith("Coding"))
#29. Does 'Coding For All' end with 'coding'?
text = "Coding For All"
print(text.endswith("coding"))
#30. Remove left and right spaces
text = "   Coding For All      "
print(text.strip())
challenge = 'thirty days of pythoonnn'
print(challenge.strip('thon'))
#31. Which variable is a valid identifier?
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
# ✅ thirty_days_of_python returns True
#32. Join list with ' # '
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))
#33. New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")
#34. Tab escape sequence
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
#35. String formatting (area of circle)
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))
#36. String formatting operations
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")














