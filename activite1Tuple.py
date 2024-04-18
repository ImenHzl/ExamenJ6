# on definit une fonction pour la liste des tuple
def tuple_plus_grand(list_tuples):
    # definir un tuple vide 
    plus_grand_tuple = ()
    max_elements = 0

    for tuple in list_tuples:
        if len(tuple) > max_elements:
            max_elements = len(tuple)
            plus_grand_tuple = tuple
    return plus_grand_tuple
# comparer la longueur de chaque tuple

liste= [(1, 2, 3), (3, 4, 5, 5, 6, 8), (6, 7, 8, 9)]

tuple_plus_grand = tuple_plus_grand(liste)

# afficher le plus grand tuple
print("Le tuple avec le plus d'éléments est :", tuple_plus_grand)
