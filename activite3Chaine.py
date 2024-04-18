# Demander de saisir le premier nombre ( sous forme de chaîne de caractères)
nombre1_str = input("Entrez le premier nombre: ")

# Demander de saisir le deuxième nombre ( sous forme de chaîne de caractères)
nombre2_str = input("Entrez le deuxième nombre: ")

# Convertir les chaînes de caractères en nombres entiers
try:    #try except pour la gestion d'erreur si l'utilisateur ne tape pas un chiffre j'affiche un message erreur.
  nombre1 = int(nombre1_str)   #j'ai utilisé la fonction int pour convertir la chaine de caract en nombre entiers.
  nombre2 = int(nombre2_str)
except ValueError:
  print("Erreur: Veuillez saisir uniquement des nombres entiers.")
  exit()  # Quitter le programme si la conversion échoue

# Effectuer l'addition des nombres
somme = nombre1 + nombre2

# Afficher le résultat
print(f"La somme de {nombre1} et {nombre2} est : {somme}")  
