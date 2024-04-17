def extraireCHaine(chainCara):
    # diviser la phrase en mot selon l'espace
    mot=chainCara.split()
    #recuperer le mot python
    pyth = mot[0]
    #recuperer le mot apprendre
    app = mot[-1]
    #recuperer la phrase langage de progarmmation de 3 à 6 position de la chaine de caractère
    phrase = mot[3:6]
    #inverser la phrase
    inverse = chainCara[::-1]
    return pyth , app , phrase , inverse
chaine1 = "Python est un langage de progarmmation puissant et facile à apprendre"
py , app , phr , inv = extraireCHaine(chaine1)
print (f"1er mot:{py}")
print (f"Avant derniere mot:{app}")
print (f"La phrase:{phr}")
print (f"La phrase inversé:{inv}")
