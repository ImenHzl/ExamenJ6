# Demander de saisir le premier nombre ( sous forme de chaîne de caractères)
nombre1_str = input("Entrez le premier nombre: ")

# Demander de saisir le deuxième nombre ( sous forme de chaîne de caractères)
nombre2_str = input("Entrez le deuxième nombre: ")

# Convertir les chaînes de caractères en nombres entiers
# try pour la gestion d'erreur si l'utilisateur ne tape pas un chiffre
try:
    # la fonction int pour convertir la chaine de caract en entiers
    nombre1 = int(nombre1_str)
    nombre2 = int(nombre2_str)
except ValueError:
    print("Erreur: Veuillez saisir uniquement des nombres entiers.")
    # Quitter le programme si la conversion échoue
    exit()

# Effectuer l'addition des nombres
somme = nombre1 + nombre2

# Affichage du résultat avec les nombres entiers :
print(f"La somme de {nombre1} et {nombre2} est : {somme}")

#Affichage du résultat avec les chaînes de caractères originales :
print(f"La somme de {nombre1_str} et {nombre2_str} est : {somme}")

#Affichage du résultat avec la concaténation de chaînes :
print("La somme de", nombre1, "et", nombre2, "est :", somme)
