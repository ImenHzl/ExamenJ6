def inverse_tuple(list):
nouvelle_liste = []

for t in list:
    tuple_inverse = i[::-1]
    nouvelle_liste.append(tuple_inverse)
    
list1=[(1,2,3) , (5,6,7) , (8,7,9)]
print("list:" , list1)
# afficher la liste avant l'inversion 

list1_inverse= inverse_tuple(list1)
print("element de tuple sont inversés :" , list1_inverse)
 