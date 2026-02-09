import turtle  # importe le module turtle pour dessiner avec une tortue graphique

'''wn = turtle.Screen()  # crée la fenêtre (screen) où la tortue va dessiner
alex = turtle.Turtle()  # crée une tortue nommée alex
alex.forward(150)  # fait avancer la tortue de 150 pixels
alex.left(90)  # fait pivoter la tortue de 90 degrés vers la gauche
alex.forward(75)'''  # fait avancer la tortue de 75 pixels
'''alex.salary = 50000  # ajoute un attribut 'salary' à la tortue alex
print(alex.salary)  # affiche la valeur de l'attribut 'salary' de la
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)'''

# wn.exitonclick()  # attend un clic dans la fenêtre pour la fermer (empêche la fermeture immédiate)


# PREMIER PROGRAMME AVEC LA TORTUE
'''window = turtle.Screen()
maria = turtle.Turtle()
maria.right(45)
maria.forward(75)
maria.left(90)
maria.forward(150)

window.exitonclick()'''

# DEUXIÈME PROGRAMME AVEC LA TORTUE
'''wn = turtle.Screen() # crée une fenêtre pour dessiner
wn.bgcolor("lightgreen") # change la couleur de fond de la fenêtre

tess = turtle.Turtle() # crée une tortue nommée tess
tess.color("blue") # change la couleur de la tortue en bleu
tess.pensize(3) # change la taille du stylo de la tortue

tess.forward(50) # fait avancer la tortue de 50 pixels
tess.left(120) # fait pivoter la tortue de 120 degrés vers la gauche
tess.forward(50) # fait avancer la tortue de 50 pixels

wn.exitonclick()'''

# TROISIÈME PROGRAMME AVEC LA TORTUE
'''wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # crée une tortue nommée tess
tess.pensize(5) # change la taille du stylo de la tortue

alex = turtle.Turtle()
alex.color("hotpink") # change la couleur de la tortue en hotpink

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(80)

alex.forward(50) # fait avancer la tortue de 50 pixels
alex.left(90) # fait pivoter la tortue de 90 degrés vers la gauche
alex.forward(50) # fait avancer la tortue de 50 pixels
alex.left(90) # fait pivoter la tortue de 90 degrés vers la gauche
alex.forward(50) # fait avancer la tortue de 50 pixels
alex.left(90) # fait pivoter la tortue de 90 degrés vers la gauche
alex.forward(50) # fait avancer la tortue de 50 pixels
alex.left(90) # fait pivoter la tortue de 90 degrés vers la gauche
alex.price = 500
tess.price = 600
print(alex.price + tess.price)

wn.exitonclick()'''

# QUATRIÈME PROGRAMME AVEC LA TORTUE

'''wn = turtle.Screen()
elan = turtle.Turtle()
distance = 50
angle = 90
for _ in range(100):
    elan.forward(distance)
    elan.right(angle)
    distance = distance + 10
    angle = angle - 3'''

# CINQUIEME PROGRAMME
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")  # définit l'apparence du curseur en forme de tortue (affiche une icône 'tortue')

dist = 5  # distance initial entre les estampilles (en pixels)
tess.up()  # relève le stylo pour ne pas tracer de ligne entre les estampilles
for _ in range(300):
    tess.stamp()  # place une empreinte de la forme actuelle de la tortue
    tess.forward(dist)  # avance de la distance courante
    tess.right(24)  # tourne de 24 degrés pour espacer radialement les estampilles
    dist = dist + 2  # augmente la distance pour élargir progressivement la spirale

wn.exitonclick()




























































