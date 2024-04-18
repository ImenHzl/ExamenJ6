def rupture(dic):
    listRupture=[]
    listTriPrix=[]
    for id_produit, details_produit in dic.items():
        for cle, valeur in details_produit.items():
            if cle=='stock' and valeur==0:
                listRupture.append(details_produit)
            if cle=='prix':
                listTriPrix=sorted(dic, valeur)
    return(listRupture,listTriPrix)
            

produits = {
    'id1': {'prix': '10', 'stock': 20},
    'id2': {'prix': '15', 'stock': 22},
    'id3': {'prix': '23', 'stock': 0},
    'id4': {'prix': '33', 'stock': 0}
}
listRep=rupture(produits)
print(listRep)