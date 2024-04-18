def tuple_plus_grand(list_tuples): #je definis une fonction pour la liste des tuple
    plus_grand_tuple = () #je definis une liste de tuple vide
    max_elements=0  #le chiffre maximum vaut 0
    
    for tuple in list_tuples: #en utilisant la boucle for pour comparer les tuples
        if len(tuple)>max_elements: #si la longueure de tuple et superieur au element maximal
            max_elements = len(tuple) #l'element maximal est egale à la longueur de tuple
            plus_grand_tuple = tuple #alors la liste vaut le tuple maximum
    
    return plus_grand_tuple #donner le resultat final 
liste = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
tuple_plus_grand=tuple_plus_grand(liste)
print("Le tuple avec le plus d'éléments est :", tuple_plus_grand) #afficher le tuple le plus grand

