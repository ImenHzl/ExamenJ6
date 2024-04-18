# Affiche une pyramide d'étoiles de la hauteur spécifiée.

# Définition de la fonction pour créer une pyramide d'étoiles
def creer_pyramide_etoile(hauteur):
# Vérifier si la hauteur est valide
  if hauteur <= 0:
    print("Erreur: La hauteur doit être un nombre entier positif.")
    return
# Boucle pour créer chaque étage de la pyramide range(debut de 1 est fini dans H+1)
  for etage in range(1, hauteur + 1):
# calculer le nombre d'espaces nécessaires pour aligner les étoiles de l'étage.
    espaces = " " * (hauteur - etage)
# calculer le nombre d'étoiles à afficher. (2*etage -1 pour assurer d'obtenir un nombre impair d'étoiles)
    etoiles = "*" * (2 * etage - 1)
# Afficher l'étage de la pyramide
    print(espaces + etoiles)

# Demander à l'utilisateur la hauteur de la pyramide
hauteur_str = input("Entrez la hauteur de la pyramide: ")

# gérer les erreurs
try:
    # Convertir la hauteur en entier    
    hauteur = int(hauteur_str)
except ValueError:
    print("Erreur: La hauteur doit être un nombre entier.")
    exit()

# appeler la function pour creer et afficher la pyramide
creer_pyramide_etoile(hauteur)
