# definir une foction de trois nombres
def trois_nombres():
    list = []
    nombre1 = int(input("Entrez le nombre : "))
    nombre2 = int(input("Entrez le nombre : "))
    nombre3 = int(input("Entrez le nombre : "))
# ajouter les trois nombres dans une liste
    list.append(nombre1)
    list.append(nombre2)
    list.append(nombre3)
    grand = list[0]
    for elt in list:
        if elt >= grand:
            grand = elt
    return grand
# comparer chaque nobre par le premier element de la liste


resultat = trois_nombres()
print(f"le nombre le plus grand est: {resultat}")
# affichage le nombre le plus grand
