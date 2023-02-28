
from modulematri import*
try:
    taille=int(input("entrer la taille de votre matrice: "))
except ValueError:
    print("veuillez entrer un entier")
    taille=int(input("entrer la taille de votre matrice: "))
    
    
    
tabmatrice=[]
for i in range(taille):
    tabmatrice.append([0]*taille)
print("ceci est une matrice d ordre: ",taille ,"x", taille)
ordre1=taille*taille
for i in range(1,taille+1):
    for j in range(1,taille+1):
        print("a{}{}".format(i,j),end=" ")
    print("")

    

for i in range(taille):
    for j in range(taille):
        tabmatrice[i][j]=int(input("entrer la valeur de a"  +str(i+1)  +str(j+1)+   ":"  ))

for i in range(taille):
    for j in range(taille):
        print(tabmatrice[i] [j],end=" ")
    print()

print("1-Affichage de la matrice")
print("2-verifier si la matrice est symetrique")
print("3-verifier si la matrice est unité ou identité")
print("4-verifier si la matrice est diagonale")
print("5-verifiez si la matrice est triangulaire superieure")
print("6-verifiez si la matrice est triangulaire inferieure")
print("7. Multiplier la matrice par un réel qu’il aura à saisir") ;
print("8. Calculer le déterminant de la matrice ;")
print("9. Calculer la matrice transposée de la matrice saisi")

try:
    choix=input("Que voulez vous faire?:  ")
except TypeError:
    print("choisissez soit 1 ,2,3,4,5,6,7,8 ou 9")
    choix=input("Que voulez vous faire?:  ")

if choix=="1":
    aff(tabmatrice,taille)                    
elif choix=="2":
    veri1(tabmatrice,taille)
elif choix=="3":
    veri2(tabmatrice,taille)
elif choix=="4":
    veri3(tabmatrice,taille)
elif choix=="5":
    veri4(tabmatrice,taille)
elif choix=="6":
    veri5(tabmatrice,taille)
elif choix=="7":
    veri6(tabmatrice,taille)
 
elif choix=="9":
   veri7(tabmatrice,taille)
print("\n")
print("oui pour continuer non pour arreter")
while choix=="1" or choix=="2" or choix=="3" or choix=="4" or choix=="5" or choix=="6" or choix=="7" or choix=="8" or choix=="9":
    choix3=input("voulez vous continuer")
    if choix3=="oui":
        choix=input("Que voulez vous faire?:  ")
        print("\n")
                
        if choix=="1":
            aff(tabmatrice,taille)                    
        elif choix=="2":
            veri1(tabmatrice,taille)
        elif choix=="3":
            veri2(tabmatrice,taille)
        elif choix=="4":
            veri3(tabmatrice,taille)
        elif choix=="5":
            veri4(tabmatrice,taille)
        elif choix=="6":
            veri5(tabmatrice,taille)
        elif choix=="7":
            veri6(tabmatrice,taille)
         
        elif choix=="9":
           veri7(tabmatrice,taille)
    elif choix3=="non":
        break