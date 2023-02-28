
tabintero=[]
tabtp=[]
tab=[[],[],[]]
tabmoyenne=[]
tabfili=[]
moyenneGL=[]
moyenneRSS=[]
moyenneCS=[]
moyenneDW=[]
moyenneWIM=[]
nombre=int(input("Entrer le nombre  d etudiants:  "))
nombretp=int(input("entrer le nombre de devoirs de maisons: "))
nombreintero=int(input("entrer le nombre d interrogation: "))
print("NB: pour un etudiant n ' ayant pas de note de tp ou de devoir de maiosn mettre 0 par defaut apres avoir renseigné le nombre")
while nombre>0 and nombreintero>0 and nombretp>0 :
    noms=input("entrer le nom de l etudiant:  ")
    fili=str(input("Filiere de l eleve:  "))
    notedevoir=float(input("entrer la note devoir:  "))
    noteintero=float(input("entrer la note d intero:"))
    notetp=float(input("enter le note de tp:"))
    noteexam=float(input("entrer la note examen: "))
    moyenneint=sum(tabintero)/nombreintero
    moyennetp=sum(tabtp)/nombretp
    moyenne=((notedevoir*0.2)+(noteexam*0.4)+(moyenneint*0.2)+(moyennetp*0.2))
    tab[0].append(noms)
    tab[1].append(notedevoir)
    tabintero.append(noteintero)
    tabtp.append(notetp)
    tab[2].append(noteexam)
    tabfili.append(fili)
    tabmoyenne.append(moyenne)
    if fili=="GL":
        moyenneGL.append(moyenne)
        print([moyenneGL])
    elif fili=="RSS":
        moyenneRSS.append(moyenne)
        print([moyenneRSS.])
    elif fili=="CS":
        moyenneCS.append(moyenne)
        print([moyenneCS])
    elif fili=="DW":
        moyenneDW.append(moyenne)
        print([moyenneDW])
    elif fili=="WIM":
        moyenneWIM.append(moyenne)
        print([moyenneWIM])
    nombre-=1
    nombreintero-=1
    nombretp-=1
globaltab=[]
globaltab.extend(moyenneGL)
globaltab.extend(moyenneCS)
globaltab.extend(moyenneRSS)
globaltab.extend(moyenneDW)
globaltab.extend(moyenneWIM)
print("les moyennes generales des filieres sont:",globaltab)
glob=sorted(globaltab,reverse=True)

print("n° \t Nom \tDevoir Surveillé \t Examen Final")
for i in range (len(tab[0])):
    print("{}\t{}\t{}\t\t{}".format(i+1,tab[0][i],tab[1][i],tab[2][i]))
print("n° \t Filiere \tMoyenne Générale")
for i in range (len(globaltab)):
    print("{}\t{}\t{}".format(i+1,tabfili[i],glob[i]))


    
print("MENU")
print("a-listes des notes des étudiants")
print("b-Liste des Moyennes Générales des étudiants.")
print("c-informations de l étudiant ou des étudiant ayant la plus forte et de l étudiant ou des étudiants ayant la plus faible moyenne generale")
print("d-Moyenne Générale Globale des étudiants dans l UE")
print("e-Nombre d étudiants ayant une moyenne generale superieur ou egale a 10 et nombre d eleve ayant une moyenne inferieur a 10")
print("f-Recherche d ' un étudiant à partir de son nom et affichage de ses informations")
print("g-affichage du tableau complet")
print("h-Moyenne générale par Filiere")
user=str(input("Que voulez-vous faire ? :"))
if user=="a":
    print("la liste des notes des étudiants est:",tab[1])
elif user=="b":
    print("la listes des Moyennes des étudiants est:",tabmoyenne)
elif user=="c":
    for i in tab[1]:
        print("la plus forte moyenne est :",max(tab[1]))
        print("la plus faible moyenne est:",min(tab[1]))
        break
elif user=="d":
     moyenne=(sum(globaltab))/(len(globaltab))
     print("La moyenne générale des élèves dans l UE est de:",moyenne)
elif user=="e":
     note=[moyenne for moyenne in tabmoyenne if moyenne<10]
     print(note)
     n2=len(note)
     print("le nombre d eleves n ayant pas la moyenne est de:",n2)
     note=[moyenne for moyenne in tabmoyenne if moyenne>10]
     print(note)
     n2=len(note)
     print("le nombre d eleves ayant la moyenne est de:",n2)
elif user=="f":
    nom2=str(input("entrer le nom de l etudiant chercher?"))
    for i in tab[0]:
        if i==nom2:
            print("la note de cette eleve est",tab[1][0])
elif user=="g":
    tab=[[],[],[]]
    tabmoyenne=[[]]
    nombre=int(input("entrer le nombre  d etudiants:  "))
    while nombre>0:
        noms=input("entrer le nom de l etudiant:  ")
        notedevoir=float(input("entrer la note devoir:  "))
        noteexam=float(input("entrer la note examen: "))
        moyenne=str((notedevoir*0.4)+(noteexam*0.6))
        tab[0].append(noms)
        tab[1].append(notedevoir)
        tab[2].append(noteexam)
        tabmoyenne[0].append(moyenne)
        nombre-=1
    print("n° \t Nom \tDevoir Surveillé \t Examen Final\t Moyenne Générale")
    for i in range (len(tab[0])):
        print("{}\t{}\t{}\t\t{}\t\t".format(i+1,tab[0][i],tab[1][i],tab[2][i]),tabmoyenne[0][i],max(tabmoyenne[0][i]))
elif user=="h":
    print("1-GL")
    print("2-CS")
    print("3-DW")
    print("4-RSS")
    print("5-WIM")
    choix4=str(input("la moyenne Globale de quelle filiere souhaitez vpous connaitre?"))

    if choix4=="1":
        moyenneglob=sum(moyenneGL)/len(moyenneGL)
        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
    elif choix4=="2":
        moyenneglob=sum(moyenneCS)/len(moyenneCS)
        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
    elif choix4=="3":
        moyenneglob=sum(moyenneDW)/len(moyenneDW)
        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
    elif choix4=="4":
        moyenneglob=sum(moyenneRSS)/len(moyenneRSS)
        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
    elif choix4=="5":
        moyenneglob=sum(moyenneWIM)/len(moyenneWIM)
        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
    while choix4=="1" or choix4=="2" or choix4=="3" or choix4=="5" or choix4=="5":
        choix5=str(input("desirez vous connaitre celle d une autre filiere"))
        if choix5=="oui":
            choix4=str(input("la moyenne Globale de quelle filiere souhaitez vpous connaitre?"))
            if choix4=="1":
                moyenneglob=sum(moyenneGL)/len(moyenneGL)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            elif choix4=="2":
                moyenneglob=sum(moyenneCS)/len(moyenneCS)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            elif choix4=="3":
                moyenneglob=sum(moyenneDW)/len(moyenneDW)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            elif choix4=="4":
                moyenneglob=sum(moyenneRSS)/len(moyenneRSS)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            elif choix4=="5":
                moyenneglob=sum(moyenneWIM)/len(moyenneWIM)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
        else:
            break
while user=="a" or user=="b" or user=="c" or user=="d" or user=="e" or user=="f" or user=="g":
    choix2=str(input("Desirez-vous continuer ?:   "))
    if choix2=="oui":
        print("a-listes des notes des étudiants")
        print("b-Liste des Moyennes Générales des étudiants.")
        print("c-informations de l étudiant ou des étudiant ayant la plus forte et de l étudiant ou des étudiants ayant la plus faible moyenne generale")
        print("d-Moyenne Générale Globale des étudiants dans l UE")
        print("e-Nombre d étudiants ayant une moyenne generale superieur ou egale a 10 et nombre d eleve ayant une moyenne inferieur a 10")
        print("f-Recherche d ' un étudiant à partir de son nom et affichage de ses informations")
        print("g-affichage du tableau complet")
        user=str(input("Que voulez-vous faire ? :"))
        if user=="a":
            print("la liste des notes des étudiants est:",tab[1])
        elif user=="b":
            print("la listes des Moyennes des étudiants est:",tabmoyenne)
        elif user=="c":
            for i in tab[1]:
                print("la plus forte moyenne est :",max(tab[1]))
                print("la plus faible moyenne est:",min(tab[1]))
                break
        elif user=="d":
                moyenne=(sum(tabmoyenne))/(len(tab[1]))
                print("La moyenne générale des élèves dans l UE est de:",moyenne)
        elif user=="e":
                note=[moyenne for moyenne in tabmoyenne if moyenne<10]
                print(note)
                n2=len(note)
                print("le nombre d eleves n ayant pas la moyenne est de:",n2)
                note=[moyenne for moyenne in tabmoyenne if moyenne>10]
                print(note)
                n2=len(note)
                print("le nombre d eleves ayant la moyenne est de:",n2)
        elif user=="f":
            nom2=str(input("entrer le nom de l etudiant chercher?"))
            for i in tab[0]:
                j=0
                while  i in tab[0][j]!= i in tab[1][j]:
                    j=j+1
                    print("la note de cet eleve est :",tab[1][j])
        elif user=="g":
        
            tab=[[],[],[]]
            tabmoyenne=[[]]
            nombre=int(input("entrer le nombre  d etudiants:  "))
            while nombre>0:
                noms=input("entrer le nom de l etudiant:  ")
                notedevoir=float(input("entrer la note devoir:  "))
                noteexam=float(input("entrer la note examen: "))
                moyenne=str((notedevoir*0.4)+(noteexam*0.6))
                tab[0].append(noms)
                tab[1].append(notedevoir)
                tab[2].append(noteexam)
                tabmoyenne[0].append(moyenne)
                nombre-=1
            print("n° \t Nom \tDevoir Surveillé \t Examen Final\t Moyenne Générale")
            for i in range (len(tab[0])):
                print("{}\t{}\t{}\t\t{}\t\t".format(i+1,tab[0][i],tab[1][i],tab[2][i]),tabmoyenne[0][i],max(tabmoyenne[0][i]))
        elif user=="h":
            print("1-GL")
            print("2-CS")
            print("3-DW")
            print("4-RSS")
            print("5-WIM")
            choix4=str(input("la moyenne Globale de quelle filiere souhaitez vpous connaitre?"))

            if choix4=="1":
                moyenneglob=sum(moyenneGL)/len(moyenneGL)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            elif choix4=="2":
                moyenneglob=sum(moyenneCS)/len(moyenneCS)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            elif choix4=="3":
                moyenneglob=sum(moyenneDW)/len(moyenneDW)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            elif choix4=="4":
                moyenneglob=sum(moyenneRSS)/len(moyenneRSS)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            elif choix4=="5":
                moyenneglob=sum(moyenneWIM)/len(moyenneWIM)
                print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
            while choix4=="1" or choix4=="2" or choix4=="3" or choix4=="5" or choix4=="5":
                choix5=str(input("desirez vous connaitre celle d une autre filiere"))
                if choix5=="oui":
                    choix4=str(input("la moyenne Globale de quelle filiere souhaitez vpous connaitre?"))
                    if choix4=="1":
                        moyenneglob=sum(moyenneGL)/len(moyenneGL)
                        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
                    elif choix4=="2":
                        moyenneglob=sum(moyenneCS)/len(moyenneCS)
                        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
                    elif choix4=="3":
                        moyenneglob=sum(moyenneDW)/len(moyenneDW)
                        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
                    elif choix4=="4":
                        moyenneglob=sum(moyenneRSS)/len(moyenneRSS)
                        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
                    elif choix4=="5":
                        moyenneglob=sum(moyenneWIM)/len(moyenneWIM)
                        print("La moyenne globale des eleves de cette filiere est:",moyenneglob)
                else:
                    break
    elif choix2=="non":
        break
    
    
        
      
    