nombres = [] #j'initialise une liste vide pour enregistrer les nombres
for i in range(3): #on veut juste trois nombre
    nombre = float(input("Entrez le nombre : ")) # 
    nombres.append(nombre)
plus_grand_nombre = nombres[0]
for nombre in nombres:
    if nombre > plus_grand_nombre:
        plus_grand_nombre = nombre
print("Le plus grand nombre parmi les nombres saisis est :", plus_grand_nombre) #affiche le nombre le plus grandcdc