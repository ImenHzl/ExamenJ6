""" Programme Py pour effectuer rotation à droite des éléments d'une liste """


# j'ai défini une fonction pour effectuer une rotation à droite d'une liste
def rotation_droite(liste, n):

    return liste[-n:] + liste[:-n]
# Effectue la rotation à droite en utilisant l'opération de slicing


# Saisie de la liste par l'utilisateur
liste_str = input("Entrez les éléments de la liste séparés par des espaces : ")

# Transformation de la chaîne en LISTE de caractères et séparation par espace
liste = liste_str.split()

# Saisie du nombre de rotations par l'utilisateur
n = int(input("Entrez le nombre de rotations à droite : "))

# le résultat est assigné à la variable liste_rot.
liste_rot = rotation_droite(liste, n)
print(f"Liste originale : {liste}")
print(f"Liste après rotation à droite de {n} positions : {liste_rot}")
