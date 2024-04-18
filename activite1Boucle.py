# BIBLIOTHEQUE pour generer des nombres aléatoires
import random


def devineNombre():
    # choisir un nombre aléatoire de 1 à 100
    nombre_aleatoire = random.randint(1, 100)
    # afficher le nombre choisi
    print(nombre_aleatoire)
    # pour limiter le nombre de tentative
    limite = 5
    # initialiser le tentative à 1
    i = 1
    # refaire le test jusqu'a 5
    while i <= limite:
        # saisir le nombre par clavier
        nombre_alt = input("Devine le nombre:")
        # si le nombre saisi est plus petit que le nombre choisi aléatoirement il affiche un message plus petit
        if int(nombre_alt) >= int(nombre_aleatoire):
            print("Le nombre est plus petit")
        # sinon il affiche le nombre est plus grand
        else:
            print("le nombre est plus grand")
        # incrementer la tentative
        i += 1


result = devineNombre()
