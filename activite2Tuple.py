# definir une fonction d'une liste des tuples
def inverse_tuple(list):
    nouvelle_liste = []
    for i in list:
        tuple_inverse = i[::-1]
        nouvelle_liste.append(tuple_inverse)
    return nouvelle_liste

list1 = [(1, 2, 3, 8), (5, 6, 7, 8), (8, 7, 9, 5)]

print("list de tuple :", list1)
# afficher la liste avant l'inversion 

# inverser les elements dans chaque tuple de la liste
list1_inverse = inverse_tuple(list1)

# afficher les tuples inversées dans la liste
print("element de tuple sont inversés :", list1_inverse)
