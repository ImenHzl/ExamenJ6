def codeCHaine(listeAsci):
    # on déclare une chaine vide
    chaine = ""
    # on fait parcourir la liste des code ascii
    for elt in listeAsci:
        # convertir le code ascii en un caractere avec chr
        mot = chr(elt)
        # on concatine les caractères et on le met dans la chaine
        chaine += mot
    return chaine


list = [65, 66, 67]
result = codeCHaine(list)
print(result)
