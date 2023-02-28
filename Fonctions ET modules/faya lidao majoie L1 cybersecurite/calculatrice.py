print("MINI CALCULATRICE")
print("1-Addition")
print("2-Soustraction")
print("3-Multiplication")
print("4-Division")

opera=int(input("Quelle operation voulez-vous effectuer ?  "))
import mod

if opera==1:
    nombre1=int(input(" veuillez entrer le nombre 1:  "))
    nombre2=int(input(" veuillez entrer le nombre 2:   "))
    mod.add(nombre1,nombre2)

elif opera==2:
    nombre1=int(input("veuillez entrer le nombre 1:  "))
    nombre2=int(input("veuillez entrer le nombre 2:   "))
    mod.soustract(nombre1,nombre2)
    
elif opera==3:
    nombre1=int(input("veuillez entrer le nombre 1:  "))
    nombre2=int(input("veuillez entrer le nombre 2:   "))
    mod.multipli(nombre1,nombre2)

elif opera==4:
    print("a-Division entiere")
    print("b-division decimale")
    choix3=str(input("Division entiere ou decimale :  ?  "))
    if choix3=="a":
        print("D'accord")
        nombre1=int(input("veuillez entrer le nombre 1:  "))
        nombre2=int(input("veuillez entrer la dividande:   "))
        mod.divi1(nombre1,nombre2)
    elif choix3=="b":
        print("ok")
        nombre1=int(input("veuillez entrer le nombre 1:  "))
        nombre2=int(input("veuillez entrer la dividande:   "))
        mod.divi2(nombre1,nombre2)
        
while opera==1 or opera==2 or opera==3 or opera==4:
   
    choix2=str(input("Desirez-vous continuer: ?  "))
    if choix2=="oui":
        opera=int(input("Quelle operation avez-vous maintenant envie de faire ? "))
        if opera==1:
            nombre1=int(input("veuillez entrer le nombre 1:  "))
            nombre2=int(input("veuillez entrer le nombre 2:   "))
            mod.add(nombre1,nombre2)

        elif opera==2:
            nombre1=int(input("veuillez entrer le nombre 1:  "))
            nombre2=int(input("veuillez entrer le nombre 2:   "))
            mod.soustract(nombre1,nombre2)
    
        elif opera==3:
            nombre1=int(input("veuillez entrer le nombre 1:  "))
            nombre2=int(input("veuillez entrer le nombre 2:   "))
            mod.multipli(nombre1,nombre2)

    
        elif opera==4:
            print("a-Division entiere")
            print("b-division decimale")
            choix3=str(input("Division entiere ou decimale :  ?  "))
            if choix3=="a":
                print("D' accord")
                nombre1=int(input("veuillez entrer le nombre 1:  "))
                nombre2=int(input("veuillez entrer la dividande:   "))
                mod.divi1(nombre1,nombre2)
            elif choix3=="b":
                print("ok")
                nombre1=int(input("veuillez entrer le nombre 1:  "))
                nombre2=int(input("veuillez entrer la dividande:   "))
                mod.divi2(nombre1,nombre2)
    elif choix2=="non":
        print("super.vous pouvez relancer la calculatrice a tous moments")
        break    
        