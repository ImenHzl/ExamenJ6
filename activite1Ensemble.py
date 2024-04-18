""" Programme Python pour trouver l'intersection de deux ensembles """

# Saisie des éléments du premier ensemble par l'utilisateur
elements1 = input("Entrez les éléments du 1ERE ensemble: ").split()

# Saisie des éléments du deuxième ensemble par l'utilisateur
elements2 = input("Entrez les éléments du 2EME ensemble: ").split()

# Création des ensembles à partir des listes d'éléments
ensemble1 = set(elements1)
ensemble2 = set(elements2)

# Création d'un ensemble vide pour stocker l'intersection
intersection = set()

# autre methode pour : intersection = ensemble1.intersection(ensemble2)

# Trouver l'intersection des deux ensembles en utilisant une boucle for
for element in ensemble1:
    if element in ensemble2:
        intersection.add(element)

# Affichage de l'intersection
print(f"L'intersection des deux ensembles est : {intersection}")
