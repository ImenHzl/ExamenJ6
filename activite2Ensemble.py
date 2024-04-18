# Saisie des éléments du premier ensemble par l'utilisateur
elements1 = input("Entrez les éléments du premier ensemble séparés par des espaces : ").split()

# Saisie des éléments du deuxième ensemble par l'utilisateur
elements2 = input("Entrez les éléments du deuxième ensemble séparés par des espaces : ").split()

# Création des ensembles à partir des listes d'éléments
ensemble1 = set(elements1)
ensemble2 = set(elements2)

# Calcul de la différence symétrique "|"" combine ces deux ensembles pour obtenir la différence symétrique complète.
difference_symetrique = (ensemble1 - ensemble2) | (ensemble2 - ensemble1)

# Affichage de la différence symétrique
print(f"La différence symétrique des deux ensembles est : {difference_symetrique}")
