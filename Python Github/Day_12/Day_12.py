# DAY_12
# Exercises: Level 1
import random
import string
#1.
'''def random_user_id():
    chars = string.ascii_letters + string.digits
    # Génère une chaîne de 10 caractères aléatoires choisis parmi les lettres et les chiffres
    return ''.join(random.choice(chars) for _ in range(10))
print(random_user_id())'''
#2.


#3.
'''def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
# random.randint(a, b). Elle génère un entier pseudo-aléatoire compris entre a et b inclusivement.
    return (r, g, b)
print(rgb_color_gen())'''

# Exercises: Level 2
#4.
'''def list_of_hexa_colors(n=1):
    hexa_colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hexa_colors.append(color)
    return hexa_colors
print(list_of_hexa_colors())

#5.
def list_of_rgb_colors(n=1):
    rgb_colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r},{g},{b})")
    return rgb_colors
print(list_of_rgb_colors())

# 6. generate_colors
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Type invalide : choisir 'hexa' ou 'rgb'."
print(generate_colors())'''

# Exercises: Level 3
# 7. shuffle_list
def shuffle_list(lst):
    shuffled = lst[:]  # copie
    random.shuffle(shuffled)
    return shuffled
print(shuffle_list([1,2,3,4,5,6]))


# 8. seven unique random numbers (0-9)
def unique_random_numbers():
    return random.sample(range(10), 7)
print(unique_random_numbers())


















