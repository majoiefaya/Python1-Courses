ht=int(input("entrer le prix hors taxe:"))#ht=prix hors taxe
na=int(input("entrer le nombre d articles:"))#na=Nombre d articles
tva=int(input("entrer la taxe sur la valeure ajoutée:"))#tva=taxe sur la valeure ajoutée
ttc=na*ht*(1+tva)#ttc=taxe toutes valeures comprises
print("le prix totale ttc est:",ttc)