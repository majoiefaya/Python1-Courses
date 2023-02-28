def aff(tabmatrice,taille):
    for i in range(taille):
        for j in range(taille):
            print(tabmatrice[i] [j],end=" ")
        print()
        
def veri1(tabmatrice,taille):
    tabmatrice2=[[tabmatrice[j][i] for j in range(taille)] for i in range(taille)]
    tabmatrice1=[[tabmatrice[i][j] for i in range(taille)] for j in range(taille)]
    if tabmatrice1!=tabmatrice2:
        print("votre matrice n est pas symetrique")
    else:
        print("votre matrice est symetrique")
        
def veri2(tabmatrice,taille):
    for i in range(taille):
        i+=1
        for j in range(taille):
            t=1
            i=0
            j=0
            if tabmatrice[i][j]!=t:
                j+=1
                print("cette matrice est unité")
                break
            else:
                print("cette matrice est identité")
                break
                
                
def veri3(tabmatrice,taille):
    op=True
    for i in range(len(tabmatrice)):
        for j in range(len(tabmatrice)):
            if(i!=j and tabmatrice[i][j]!=0):
                op=False
    if(op==True):
        print("la matrice est diagonalisable")
    else:
        print("la matrice n est pas diagonalisable")

def veri4(tabmatrice,taille):
     for i in range(taille):
        i+=1
        for j in range(taille):
            t=0
            i=0
            j=1
            if tabmatrice[i][j]==t:
                j+=1
                print("cette matrice est triangulaire superieur")
                break
            else:
                print("cette matrice n est pas triangulaire superieur")
                break
def veri5(tabmatrice,taille):
    for i in range(taille):
        i+=1
        for j in range(taille):
            t=0
            i=1
            j=0
            if tabmatrice[i][j]==t:
                j+=1
                print("cette matrice est triangulaire inferieur")
                break
            else:
                print("cette matrice n est pas triangulaire inferieur")
                break
def veri6(tabmatrice,taille):
    choix2=int(input("entrer le réel avec lequel vous desirez \n multiplier la matrice: \n "))
    print("le resultat de l operation est:\n  ")
    for i in range(taille):
        for j in range(taille):
            print(choix2*(tabmatrice[i] [j]),end=" ")
        print()
def veri7(tabmatrice,taille):
    print("votre matrice transposée est:")
    for i in range(taille):
        for j in range(taille):
            print(tabmatrice[j] [i],end=" ")
        print()
    