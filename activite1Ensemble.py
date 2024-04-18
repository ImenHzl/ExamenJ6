# Saisie des éléments du premier ensemble par l'utilisateur
elements1 = input("Entrez les éléments du premier ensemble séparés par des espaces : ").split()

# Saisie des éléments du deuxième ensemble par l'utilisateur
elements2 = input("Entrez les éléments du deuxième ensemble séparés par des espaces : ").split()

# Création des ensembles à partir des listes d'éléments
ensemble1 = set(elements1)
ensemble2 = set(elements2)

# Initialisation de l'ensemble pour stocker l'intersection
intersection = set()

# Trouver l'intersection des deux ensembles en utilisant une boucle for
for element in ensemble1:
    if element in ensemble2:
        intersection.add(element)

# Affichage de l'intersection
print(f"L'intersection des deux ensembles est : {intersection}")
