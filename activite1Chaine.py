def chaineCar(chain):   
    nbrMaj = 0
    nbrMin = 0
    #boucle sur chaque caractere de la chaine qu'on a saisi
    for i in chain:
        #si le caractere est majuscule on va incrementer nbrMaj
        if i.isupper():
            nbrMaj += 1
        #si le caractere est miniscule on va incrementer nbrMin
        else:
            nbrMin += 1
    return nbrMaj,nbrMin
chaine = input("entrez une chaine de caractère: ")
maj,min = chaineCar(chaine)
print(f"nombre Majuscule:{maj}")
print(f"nombre Miniscule:{min}")