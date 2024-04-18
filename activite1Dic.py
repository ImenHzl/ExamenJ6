def moyenne(dic):
    dicMoy = {}
# creer un nouveau dictionnaire
# parcourir le dictionnaire
    for cle, valeur in dic:
        # vérifier si la valeur (moyen) est supérieur a 15
        if valeur >= 15:
            # ajouter le nom et le moyen plus de 15 dans le dicMoy
            dicMoy[cle] = valeur
# return le nouveau dic avec persoone de moyen plus de 15
    return dicMoy


dic = {("Imen", 16), ("Rayan", 18), ("Mira", 19), ("walid", 14)}
resultat = moyenne(dic)
print(resultat)
