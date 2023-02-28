
fichier=open("gestion.txt","r")
contenu=fichier.read()
if contenu=='':
    print("le fichier est vide")
    tab=[[],[],[]]
    tabmoyenne=[]
    try:
        nombre=int(input("entrer le nombre  d etudiants:  "))
    except ValueError:
        print("erreur de saisie")
        nombre=int(input("entrer le nombre  d etudiants:  "))
    while nombre>0:
        noms=input("entrer le nom de l etudiant:  ")  
        notedevoir=float(input("entrer la note devoir:  "))
        noteexam=float(input("entrer la note examen: "))
        moyenne=(notedevoir*0.4)+(noteexam*0.6)
        tab[0].append(noms)
        tab[1].append(notedevoir)
        tab[2].append(noteexam)
        tabmoyenne.append(moyenne)
        fichier=open("gestion.txt", "w")
        note=open("note devoir.txt","w")
        exam=open("Note Exam.txt","w")
        nom=open("nom.txt","w")
        moyenne=open("moyenne.txt","w")
        nom.write(str(tab[0]))
        nom.write("\n")
        fichier.write(str(tab[0]))
        fichier.write("\n")
        note.write(str(tab[1]))
        note.write("\n")
        fichier.write(str(tab[1]))
        fichier.write("\n")
        exam.write(str(tab[2]))
        exam.write("\n")
        fichier.write(str(tabmoyenne))
        fichier.write("\n")
        moyenne.write(str(tabmoyenne))
        moyenne.write("\n")
        fichier.close()
        nom.close()
        note.close()
        exam.close()
        moyenne.close()
        nombre-=1
    print("n° \t Nom \tDevoir Surveillé \t Examen Final")
    for i in range (len(tab[0])):
        print("{}\t{}\t{}\t\t{}".format(i+1,tab[0][i],tab[1][i],tab[2][i]))
    print("MENU")
    print("a-listes des notes des étudiants")
    print("b-Liste des Moyennes Générales des étudiants.")
    print("c-informations de l étudiant ou des étudiant ayant la plus forte et de l étudiant ou des étudiants ayant la plus faible moyenne generale")
    print("d-Moyenne Générale Globale des étudiants dans l UE")
    print("e-Nombre d étudiants ayant une moyenne generale superieur ou egale a 10 et nombre d eleve ayant une moyenne inferieur a 10")
    print("f-Recherche d ' un étudiant à partir de son nom et affichage de ses informations")
    print("g-affichage du tableau complet")
    print("h-Moyenne générale par Filiere")
    print("i--ajout d une information")
    print("j-modification")
    print("k-Suppression")
    user=str(input("Que voulez-vous faire ? :"))
    if user=="a":
        print("la liste des notes des étudiants est:",tab[1])
    elif user=="b":
        print("la listes des Moyennes des étudiants est:",tabmoyenne)
    elif user=="c":
        for i in range (len(tabmoyenne)):
            maxnote=max(tabmoyenne)
            if maxnote==tabmoyenne[i]:
                   print("le nom de cet eleve est:",tab[0][i])
                   print("la note de devoir de cet eleve est:",tab[1][i])
                   print("la note d' Examen de cet  eleve est:",tab[2][i])
                   print("la moyenne génerale de cet eleve est:",tabmoyenne[i])
        for i in range (len(tabmoyenne)):
            minnote=min(tabmoyenne)
            if minnote==tabmoyenne[i]:
                   print("le nom de cet eleve est:",tab[0][i])
                   print("la note de devoir de cet eleve est:",tab[1][i])
                   print("la note d' Examen de cet eleve est:",tab[2][i])
                   print("la moyenne génerale de cet eleve est:",tabmoyenne[i])
    elif user=="d":
            d=open("d.txt","w")
            moyenne=(sum(tabmoyenne))/(len(tab[1]))
            print("La moyenne générale des élèves dans l UE est de:",moyenne)
            d.write(str(moyenne))
            d.close()
    elif user=="e":
         e=open("e.txt","w")
         note=[moyenne for moyenne in tabmoyenne if moyenne<10]
         print(note)
         n2=len(note)
         print("le nombre d eleves n ayant pas la moyenne est de:",n2)
         note=[moyenne for moyenne in tabmoyenne if moyenne>10]
         print(note)
         n3=len(note)
         print("le nombre d eleves ayant la moyenne est de:",n3)
         e.write("les eleves n ayant pas la moyenne est \t:")
         e.write(str(n2))
         e.write("\n")
         e.write("les eleves ayant pas la moyenne est \t:")
         e.write(str(n3))
         e.close()
    elif user=="f":
         nom2=str(input("entrer le nom de l etudiant chercher?"))
         if tab[0][i]==nom2:
            f=open("f.txt","w")
            print("la note de devoir de",nom2," est:",tab[1][i])
            print("la note d' Examen de",nom2," est:",tab[2][i])
            print("la moyenne génerale de",nom2," est:",tabmoyenne[i])
            f.write("la note de devoir de cet eleve est \t")
            f.write(str(tab[1][i]))
            f.write("\n")
            f.write("la note d' examen de cet eleve est \t")
            f.write(str(tab[2][i]))
            f.write("\n")
            f.write("la moyenne generale de cet eleve est \t")
            f.write(str(tabmoyenne[i]))
            f.close()
              
                    
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
            print("{}\t{}\t{}\t{}\{}\t\t{}".format(i+1,tab[0][i],tab[1][i],tabtp[i],tab[2][i],tabmoyenne[i]))


    elif user=="i":
        print("choisir\n\ta- ajouter une seule information\nb-ajout complet(nom,note devoir,exam,etc..")
        choix5=input("Que voulez vous ajouter?: ")
        if choix5=="a":
            choix6=input("Quelle information voulez vous ajouter?")
            if choix6=="nom":
                newname=input("Quelle nom voulez vous ajouter?: ")
                tab[0].append(newname)
                print("nom ajoutée")
            elif choix6=="devoir":
                    newdev=float(input("Quelle note voulez vous ajouter?: "))
                    tab[1].append(newdev)
                    print("note ajoutée")
            elif choix6=="exam":
                    newex=float(input("Quelle note d examen voulez vous ajouter?: "))
                    tab[2].append(newex)
                    print("note  d examen ajoutée")    
            elif choix6=="notetp":
                    tabtp=[]
                    for i in range (len(tab[1])):
                        new=float(input("entrer 0"))
                        tabtp.append(new)
                    print("Voici les noms de vos eleves",tab[0])
                    choix7=input("A quel éleve voulez vous ajouter cette information")
                    index=tab[0].index(choix7)
                    newtp=float(input("entrer la note: "))
                    tabtp[index]=newtp
                    print("l information a bien été ajoutée a l elève")
            elif choix6=="noteintero":
                    tabint=[]
                    for i in range (len(tab[1])):
                        new=float(input("entrer  un null(0):   "))
                        tabint.append(new)
                    print("Voici les noms de vos eleves",tab[0])
                    choix7=input("A quel éleve voulez vous ajouter cette information")
                    index=tab[0].index(choix7)
                    newint=float(input("entrer la note: "))
                    tabint[index]=newint
                    print("l information a bien été ajoutée a l elève")




        elif choix5=="b":
            nombre2=int(input("entrer le nombre  d etudiants:  "))
            nombre3=nombre+nombre2
            while nombre2>0:
                noms=input("entrer le nom de l etudiant:  ")
                notedevoir=float(input("entrer la note devoir:  "))
                noteexam=float(input("entrer la note examen: "))
                moyenne=(notedevoir*0.4)+(noteexam*0.6)
                tab[0].append(noms)
                tab[1].append(notedevoir)
                tab[2].append(noteexam)
                tabmoyenne.append(moyenne)
                nombre2-=1            
        
    elif user=="j":
        print("choisir\n\ta-une seule information\nb-informations completes(nom,note devoir,exam,etc..")
        choix5=input("Que voulez vous modifiez? ")
        if choix5=="a":
            print("nom:modifier le nom\ndevoir:modifier la note de devoir\nexam:modifier la note d examen")
            choix6=input("Quelle information voulez vous modifier")
            if choix6=="nom" or choix6=="Nom":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("Quel nom voulez vous modifier ou remplacer? ")
                newname=input("Veuillez entrer le nouveau Nom")
                index=tab[0].index(choix7)
                tab[0][index]=newname
                print("nom modifié",tab[0])
            elif choix6=="devoir":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                index=tab[0].index(choix7)
                newnoteds=float(input("Veuillez entrer la nouvelle note de devoir"))
                tab[1][index]=newnoteds
                print("Note de devoir  modifiée",tab[1])
            elif choix6=="exam":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("la note d' examen de quel etudiant voulez vous modifier ou remplacer? ")
                index=tab[0].index(choix7)
                newnoteexam=float(input("Veuillez entrer la nouvelle note d' examen"))
                tab[2][index]=newnoteexam
                print("Note d' examen  modifiée",tab[2])
            elif choix6=="notetp":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                index=tab[0].index(choix7)
                newnotetp=float(input("Veuillez entrer la nouvelle note de tp"))
                tabtp[index]=newnotetp
                print("Note de tp  modifiée",tabtp)
            elif choix6=="interro":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                index=tab[0].index(choix7)
                newnoteint=float(input("Veuillez entrer la nouvelle note de devoir"))
                tabint[index]=newnoteint
                print("Note d interro modifiée",tabint)
        elif choix5=="b":
            choix6=input("entrer le nom de l etudiant dont vous voulez modifier les informations")
            index=tab[0].index(choix6)
            newnoteds=float(input("entrer sa nouvelle note de devoir"))
            newnoteexam=float(input("entrer sa nouvelle note d  Exam"))
            tab[1][index]=newnoteds
            tab[2][index]=newnoteexam
            print("les informations ont bien été modifieés")
        
        if choix5=="b":
            choix6=input("entrer le nom de l etudiant dont vous voulez modifier les informations")
            index=tab[0].index(choix6)
            newnoteds
            tab[0][index]=new
            print(tab[0])
    elif user=="k":
        print("choisir\n\ta- supprimer une seule information\n \tb-supprimer les informations completes(nom,note devoir,exam,etc..")
        choix5=input("Que voulez vous supprimer? ")
        if choix5=="a":
            print("nom:supprimer le nom\ndevoir:supprimerla note de devoir\nexam:supprimer la note d examen")
            choix6=input("Quelle information voulez vous supprimer")
            if choix6=="nom" or choix6=="Nom":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("Quel nom voulez vous supprimer? ")
                index=tab[0].index(choix7)
                del(tab[0][index])
                print("nom supprimé",tab[0])
            elif choix6=="devoir":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("la note de devoir de quel etudiant voulez vous supprimer? ")
                index=tab[0].index(choix7)
                del(tab[1][index])
                print("Note de devoir  supprimée",tab[1])
            elif choix6=="exam":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("la note d' examen de quel etudiant voulez vous supprimer? ")
                index=tab[0].index(choix7)
                del(tab[2][index])
                print("Note d' examen  supprimée",tab[2])
            elif choix6=="notetp":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("la note de devoir de quel etudiant voulez vous supprimer? ")
                index=tab[0].index(choix7)
                del(tabtp[index])
                print("Note de tp supprimée",tabtp)
            elif choix6=="interro":
                print("Voici les noms de vos eleves",tab[0])
                choix7=input("la note d' interrogation de quel etudiant voulez vous supprimer? ")
                index=tab[0].index(choix7)
                del(tabint[index])
                print("Note d interrogation supprimée",tabint)
        elif choix5=="b":
            print("Voici les noms de vos eleves",tab[0])
            choix6=input("entrer le nom de l etudiant dont vous voulez supprimer les informations")
            index=tab[0].index(choix6)
            del(tab[0][index])
            del(tab[1][index])
            del(tab[2][index])
            print("les informations ont bien été supprimées")

    while user=="a" or user=="b" or user=="c" or user=="d" or user=="e" or user=="f" or user=="g" or user=="i" or user=="j" or user=="k":
        choix2=str(input("Desirez-vous continuer ?:   "))
        if choix2=="oui":
            print("a-listes des notes des étudiants")
            print("b-Liste des Moyennes Générales des étudiants.")
            print("c-informations de l étudiant ou des étudiant ayant la plus forte et de l étudiant ou des étudiants ayant la plus faible moyenne generale")
            print("d-Moyenne Générale Globale des étudiants dans l UE")
            print("e-Nombre d étudiants ayant une moyenne generale superieur ou egale a 10 et nombre d eleve ayant une moyenne inferieur a 10")
            print("f-Recherche d ' un étudiant à partir de son nom et affichage de ses informations")
            print("g-affichage du tableau complet")
            print("i--ajout d une information")
            print("j-modification")
            print("k-Suppression")
            user=str(input("Que voulez-vous faire ? :"))
            if user=="a":
                print("la liste des notes des étudiants est:",tab[1])
            elif user=="b":
                print("la listes des Moyennes des étudiants est:",tabmoyenne)
            elif user=="c":
                for i in range (len(tabmoyenne)):
                    maxnote=max(tabmoyenne)
                    if maxnote==tabmoyenne[i]:
                           print("le nom de cet eleve est:",tab[0][i])
                           print("la note de devoir de cet eleve est:",tab[1][i])
                           print("la note d' Examen de cet  eleve est:",tab[2][i])
                           print("la moyenne génerale de cet eleve est:",tabmoyenne[i])
                for i in range (len(tabmoyenne)):
                    minnote=min(tabmoyenne)
                    if minnote==tabmoyenne[i]:
                           print("le nom de cet eleve est:",tab[0][i])
                           print("la note de devoir de cet eleve est:",tab[1][i])
                           print("la note d' Examen de cet eleve est:",tab[2][i])
                           print("la moyenne génerale de cet eleve est:",tabmoyenne[i])
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
                 if tab[0][i]==nom2:
                     
                            
                    print("la note de devoir de",nom2," est:",tab[1][i])
                    print("la note d' Examen de",nom2," est:",tab[2][i])
                    print("la moyenne génerale de",nom2," est:",tabmoyenne[i])
                            
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
                    print("{}\t{}\t{}\t{}\{}\t\t{}".format(i+1,tab[0][i],tab[1][i],tabtp[i],tab[2][i],tabmoyenne[i]))


            elif user=="i":
                print("choisir\n\ta- ajouter une seule information\nb-ajout complet(nom,note devoir,exam,etc..")
                choix5=input("Que voulez vous ajouter?: ")
                if choix5=="a":
                    choix6=input("Quelle information voulez vous ajouter?")
                    if choix6=="nom":
                        newname=input("Quelle nom voulez vous ajouter?: ")
                        tab[0].append(newname)
                        print("nom ajoutée")
                    elif choix6=="devoir":
                            newdev=float(input("Quelle note voulez vous ajouter?: "))
                            tab[1].append(newdev)
                            print("note ajoutée")
                    elif choix6=="exam":
                            newex=float(input("Quelle note d examen voulez vous ajouter?: "))
                            tab[2].append(newex)
                            print("note  d examen ajoutée")    
                    elif choix6=="notetp":
                            tabtp=[]
                            for i in range (len(tab[1])):
                                new=float(input("entrer 0"))
                                tabtp.append(new)
                            print("Voici les noms de vos eleves",tab[0])
                            choix7=input("A quel éleve voulez vous ajouter cette information")
                            index=tab[0].index(choix7)
                            newtp=float(input("entrer la note: "))
                            tabtp[index]=newtp
                            print("l information a bien été ajoutée a l elève")
                    elif choix6=="noteintero":
                            tabint=[]
                            for i in range (len(tab[1])):
                                new=float(input("entrer  un null(0):   "))
                                tabint.append(new)
                            print("Voici les noms de vos eleves",tab[0])
                            choix7=input("A quel éleve voulez vous ajouter cette information")
                            index=tab[0].index(choix7)
                            newint=float(input("entrer la note: "))
                            tabint[index]=newint
                            print("l information a bien été ajoutée a l elève")




                elif choix5=="b":
                    nombre2=int(input("entrer le nombre  d etudiants:  "))
                    nombre3=nombre+nombre2
                    while nombre2>0:
                        noms=input("entrer le nom de l etudiant:  ")
                        notedevoir=float(input("entrer la note devoir:  "))
                        noteexam=float(input("entrer la note examen: "))
                        moyenne=(notedevoir*0.4)+(noteexam*0.6)
                        tab[0].append(noms)
                        tab[1].append(notedevoir)
                        tab[2].append(noteexam)
                        tabmoyenne.append(moyenne)
                        nombre2-=1            
                
            elif user=="j":
                print("choisir\n\ta-une seule information\nb-informations completes(nom,note devoir,exam,etc..")
                choix5=input("Que voulez vous modifiez? ")
                if choix5=="a":
                    print("nom:modifier le nom\ndevoir:modifier la note de devoir\nexam:modifier la note d examen")
                    choix6=input("Quelle information voulez vous modifier")
                    if choix6=="nom" or choix6=="Nom":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("Quel nom voulez vous modifier ou remplacer? ")
                        newname=input("Veuillez entrer le nouveau Nom")
                        index=tab[0].index(choix7)
                        tab[0][index]=newname
                        print("nom modifié",tab[0])
                    elif choix6=="devoir":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                        index=tab[0].index(choix7)
                        newnoteds=float(input("Veuillez entrer la nouvelle note de devoir"))
                        tab[1][index]=newnoteds
                        print("Note de devoir  modifiée",tab[1])
                    elif choix6=="exam":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("la note d' examen de quel etudiant voulez vous modifier ou remplacer? ")
                        index=tab[0].index(choix7)
                        newnoteexam=float(input("Veuillez entrer la nouvelle note d' examen"))
                        tab[2][index]=newnoteexam
                        print("Note d' examen  modifiée",tab[2])
                    elif choix6=="notetp":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                        index=tab[0].index(choix7)
                        newnotetp=float(input("Veuillez entrer la nouvelle note de tp"))
                        tabtp[index]=newnotetp
                        print("Note de tp  modifiée",tabtp)
                    elif choix6=="interro":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                        index=tab[0].index(choix7)
                        newnoteint=float(input("Veuillez entrer la nouvelle note de devoir"))
                        tabint[index]=newnoteint
                        print("Note d interro modifiée",tabint)
                elif choix5=="b":
                    choix6=input("entrer le nom de l etudiant dont vous voulez modifier les informations")
                    index=tab[0].index(choix6)
                    newnoteds=float(input("entrer sa nouvelle note de devoir"))
                    newnoteexam=float(input("entrer sa nouvelle note d  Exam"))
                    tab[1][index]=newnoteds
                    tab[2][index]=newnoteexam
                    print("les informations ont bien été modifieés")
                
                if choix5=="b":
                    choix6=input("entrer le nom de l etudiant dont vous voulez modifier les informations")
                    index=tab[0].index(choix6)
                    newnoteds
                    tab[0][index]=new
                    print(tab[0])
            elif user=="k":
                print("choisir\n\ta- supprimer une seule information\n \tb-supprimer les informations completes(nom,note devoir,exam,etc..")
                choix5=input("Que voulez vous supprimer? ")
                if choix5=="a":
                    print("nom:supprimer le nom\ndevoir:supprimerla note de devoir\nexam:supprimer la note d examen")
                    choix6=input("Quelle information voulez vous supprimer")
                    if choix6=="nom" or choix6=="Nom":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("Quel nom voulez vous supprimer? ")
                        index=tab[0].index(choix7)
                        del(tab[0][index])
                        print("nom supprimé",tab[0])
                    elif choix6=="devoir":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("la note de devoir de quel etudiant voulez vous supprimer? ")
                        index=tab[0].index(choix7)
                        del(tab[1][index])
                        print("Note de devoir  supprimée",tab[1])
                    elif choix6=="exam":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("la note d' examen de quel etudiant voulez vous supprimer? ")
                        index=tab[0].index(choix7)
                        del(tab[2][index])
                        print("Note d' examen  supprimée",tab[2])
                    elif choix6=="notetp":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("la note de devoir de quel etudiant voulez vous supprimer? ")
                        index=tab[0].index(choix7)
                        del(tabtp[index])
                        print("Note de tp supprimée",tabtp)
                    elif choix6=="interro":
                        print("Voici les noms de vos eleves",tab[0])
                        choix7=input("la note d' interrogation de quel etudiant voulez vous supprimer? ")
                        index=tab[0].index(choix7)
                        del(tabint[index])
                        print("Note d interrogation supprimée",tabint)
                elif choix5=="b":
                    print("Voici les noms de vos eleves",tab[0])
                    choix6=input("entrer le nom de l etudiant dont vous voulez supprimer les informations")
                    index=tab[0].index(choix6)
                    del(tab[0][index])
                    del(tab[1][index])
                    del(tab[2][index])
                    print("les informations ont bien été supprimées")
           
        elif choix2=="non":
            break
        
        
        
      

else:
    tab=[[],[],[]]
    tabmoyenne=[]
    print("MENU")
    print("a-listes des notes des étudiants")
    print("b-Liste des Moyennes Générales des étudiants.")
    print("c-informations de l étudiant ou des étudiant ayant la plus forte et de l étudiant ou des étudiants ayant la plus faible moyenne generale")
    print("d-Moyenne Générale Globale des étudiants dans l UE")
    print("e-Nombre d étudiants ayant une moyenne generale superieur ou egale a 10 et nombre d eleve ayant une moyenne inferieur a 10")
    print("f-Recherche d ' un étudiant à partir de son nom et affichage de ses informations")
    print("g-affichage du tableau complet")
    print("h-Moyenne générale par Filiere")
    print("i--ajout d une information")
    print("j-modification")
    print("k-Suppression")


    fichier=open("gestion.txt","r")
    contenu=open("gestion.txt","r")
    f=open("f.txt","r")
    d=open("d.txt","r")
    e=open("e.txt","r")
    econt=e.read()
    fcont=f.read()
    dcont=d.read()
    contenu=contenu.read()
    contenu2=contenu.split(",")
    moyenne=open("moyenne.txt","r")
    contenu=moyenne.read()
    contenu2=contenu.split()
    note=open("note devoir.txt","r")
    note=note.read()
    note2=note.split()
    nom=open("nom.txt","r")
    nom=nom.read()
    nom2=nom.split()
    exam=open("Note Exam.txt","r")
    exam=exam.read()
    exam2=exam.split()
    
    user=str(input("Que voulez-vous faire ? :"))
    if user=="a":
        note=open("note devoir.txt","r")
        note=note.read()
        print("la liste des notes des étudiants est:",note)
    elif user=="b":
        moyenne=open("moyenne.txt","r")
        contenu=moyenne.read()
        print("la listes des Moyennes des étudiants est:",contenu)
    elif user=="c":
        for i in range (len(contenu2)):
            maxnote=max(contenu2)
            if maxnote==contenu2[i]:
                   print("la plus forte moyenne general")
                   print("le nom de cet eleve est:",nom2[i])
                   print("la note de devoir de cet eleve est:",note2[i])
                   print("la note d' Examen de cet  eleve est:",exam2[i])
                   print("la moyenne génerale de cet eleve est:",contenu2[i])
        for i in range (len(contenu2)):
            minnote=min(contenu2)
            if minnote==contenu2[i]:
                   print("la plus faible moyenne generale")
                   print("le nom de cet eleve est:",nom2[i])
                   print("la note de devoir de cet eleve est:",note2[i])
                   print("la note d' Examen de cet eleve est:",exam2[i])
                   print("la moyenne génerale de cet eleve est:",contenu2[i])
    elif user=="d":
        print(dcont)

    elif user=="e":
        if econt=="":
            print("le fichier est vide")
        else:
            print(econt)
    elif user=="f":
        if fcont=="":
            print("le fichier est vide")
        else:
            print(fcont)
    elif user=="g":
        print("n° \t Nom \tDevoir Surveillé \t Examen Final\t Moyenne Générale")
        for i in range (len(contenu2)):
            print("{}\t{}\t{}\t{}\t{}".format(i+1,nom2[i],note2[i],exam2[i],contenu2[i]))


    elif user=="i":
        print("choisir\n\ta- ajouter une seule information\nb-ajout complet(nom,note devoir,exam,etc..")
        choix5=input("Que voulez vous ajouter?: ")
        if choix5=="a":
            choix6=input("Quelle information voulez vous ajouter?")
            if choix6=="nom":
                newname=input("Quelle nom voulez vous ajouter?: ")
                nom2.append(newname)
                print("nom ajoutée")
            elif choix6=="devoir":
                    newdev=float(input("Quelle note voulez vous ajouter?: "))
                    note2.append(newdev)
                    print("note ajoutée")
            elif choix6=="exam":
                    newex=float(input("Quelle note d examen voulez vous ajouter?: "))
                    exam2.append(newex)
                    print("note  d examen ajoutée")    
            elif choix6=="notetp":
                    tabtp=[]
                    for i in range (len(nom2)):
                        new=float(input("entrer 0"))
                        tabtp.append(new)
                    print("Voici les noms de vos eleves",nom2)
                    choix7=input("A quel éleve voulez vous ajouter cette information")
                    index=nom2.index(choix7)
                    newtp=float(input("entrer la note: "))
                    tabtp[index]=newtp
                    print("l information a bien été ajoutée a l elève")
            elif choix6=="noteintero":
                    tabint=[]
                    for i in range (len(nom2)):
                        new=float(input("entrer  un null(0):   "))
                        tabint.append(new)
                    print("Voici les noms de vos eleves",nom2)
                    choix7=input("A quel éleve voulez vous ajouter cette information")
                    index=nom2.index(choix7)
                    newint=float(input("entrer la note: "))
                    tabint[index]=newint
                    print("l information a bien été ajoutée a l elève")




        elif choix5=="b":
            nombre=len(exam2)
            nombre2=int(input("entrer le nombre  d etudiants:  "))
            nombre3=nombre+nombre2
            while nombre2>0:
                noms=input("entrer le nom de l etudiant:  ")
                notedevoir=float(input("entrer la note devoir:  "))
                noteexam=float(input("entrer la note examen: "))
                moyenne=(notedevoir*0.4)+(noteexam*0.6)
                nom2.append(noms)
                note2.append(notedevoir)
                exam2.append(noteexam)
                contenu2.append(moyenne)
                nombre2-=1
                
            print("n° \t Nom \tDevoir Surveillé \t Examen Final")
            for i in range (nombre3):
                print("{}\t{}\t{}\t{}\t{}".format(i+1,nom2[i],note2[i],exam2[i],contenu2[i]))
            print("Les informations ont bien étés ajoutées")

            
        
    elif user=="j":
        print("choisir\n\ta-une seule information\nb-informations completes(nom,note devoir,exam,etc..")
        choix5=input("Que voulez vous modifiez? ")
        if choix5=="a":
            print("nom:modifier le nom\ndevoir:modifier la note de devoir\nexam:modifier la note d examen")
            choix6=input("Quelle information voulez vous modifier")
            if choix6=="nom" or choix6=="Nom":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("Quel nom voulez vous modifier ou remplacer? ")
                newname=input("Veuillez entrer le nouveau Nom")
                index=nom2.index(choix7)
                nom2[index]=newname
                print("nom modifié",nom2)
            elif choix6=="devoir":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                index=nom2.index(choix7)
                newnoteds=float(input("Veuillez entrer la nouvelle note de devoir"))
                note2[index]=newnoteds
                print("Note de devoir  modifiée",note2)
            elif choix6=="exam":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("la note d' examen de quel etudiant voulez vous modifier ou remplacer? ")
                index=nom2.index(choix7)
                newnoteexam=float(input("Veuillez entrer la nouvelle note d' examen"))
                exam2[index]=newnoteexam
                print("Note d' examen  modifiée",exam2)
            elif choix6=="notetp":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                index=nom2.index(choix7)
                newnotetp=float(input("Veuillez entrer la nouvelle note de tp"))
                tabtp[index]=newnotetp
                print("Note de tp  modifiée",tabtp)
            elif choix6=="interro":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                index=nom2.index(choix7)
                newnoteint=float(input("Veuillez entrer la nouvelle note de devoir"))
                tabint[index]=newnoteint
                print("Note d interro modifiée",tabint)
        elif choix5=="b":
            choix6=input("entrer le nom de l etudiant dont vous voulez modifier les informations")
            index=nom2.index(choix6)
            newnoteds=float(input("entrer sa nouvelle note de devoir"))
            newnoteexam=float(input("entrer sa nouvelle note d  Exam"))
            note2[index]=newnoteds
            exam2[index]=newnoteexam
            print("les informations ont bien été modifieés")
    elif user=="k":
        print("choisir\n\ta- supprimer une seule information\n \tb-supprimer les informations completes(nom,note devoir,exam,etc..")
        choix5=input("Que voulez vous supprimer? ")
        if choix5=="a":
            print("nom:supprimer le nom\ndevoir:supprimerla note de devoir\nexam:supprimer la note d examen")
            choix6=input("Quelle information voulez vous supprimer")
            if choix6=="nom" or choix6=="Nom":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("Quel nom voulez vous supprimer? ")
                index=nom2.index(choix7)
                del(nom2[index])
                print("nom supprimé",nom2)
            elif choix6=="devoir":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("la note de devoir de quel etudiant voulez vous supprimer? ")
                index=nom2.index(choix7)
                del(note2[index])
                print("Note de devoir  supprimée",note2)
            elif choix6=="exam":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("la note d' examen de quel etudiant voulez vous supprimer? ")
                index=nom2.index(choix7)
                del(exam2[index])
                print("Note d' examen  supprimée",exam2)
            elif choix6=="notetp":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("la note de devoir de quel etudiant voulez vous supprimer? ")
                index=nom2.index(choix7)
                del(tabtp[index])
                print("Note de tp supprimée",tabtp)
            elif choix6=="interro":
                print("Voici les noms de vos eleves",nom2)
                choix7=input("la note d' interrogation de quel etudiant voulez vous supprimer? ")
                index=nom2.index(choix7)
                del(tabint[index])
                print("Note d interrogation supprimée",tabint)
        elif choix5=="b":
            print("Voici les noms de vos eleves",nom2)
            choix6=input("entrer le nom de l etudiant dont vous voulez supprimer les informations")
            index=nom2.index(choix6)
            del(nom2[index])
            del(note2[index])
            del(exam2[index])
            print("les informations ont bien été supprimées")

    while user=="a" or user=="b" or user=="c" or user=="d" or user=="e" or user=="f" or user=="g" or user=="i" or user=="j" or user=="k":
        choix2=str(input("Desirez-vous continuer ?:   "))
        if choix2=="oui":
            print("a-listes des notes des étudiants")
            print("b-Liste des Moyennes Générales des étudiants.")
            print("c-informations de l étudiant ou des étudiant ayant la plus forte et de l étudiant ou des étudiants ayant la plus faible moyenne generale")
            print("d-Moyenne Générale Globale des étudiants dans l UE")
            print("e-Nombre d étudiants ayant une moyenne generale superieur ou egale a 10 et nombre d eleve ayant une moyenne inferieur a 10")
            print("f-Recherche d ' un étudiant à partir de son nom et affichage de ses informations")
            print("g-affichage du tableau complet")
            print("i--ajout d une information")
            print("j-modification")
            print("k-Suppression")
            user=str(input("Que voulez-vous faire ? :"))
            tab=[[],[],[]]
            tabmoyenne=[]
            fichier=open("gestion.txt","r")
            contenu=open("gestion.txt","r")
            contenu=contenu.read()
            contenu2=contenu.split(",")
            moyenne=open("moyenne.txt","r")
            contenu=moyenne.read()
            contenu2=contenu.split()
            note=open("note devoir.txt","r")
            note=note.read()
            note2=note.split()
            nom=open("nom.txt","r")
            nom=nom.read()
            nom2=nom.split()
            exam=open("Note Exam.txt","r")
            exam=exam.read()
            exam2=exam.split()
            user=str(input("Que voulez-vous faire ? :"))
            if user=="a":
                note=open("note devoir.txt","r")
                note=note.read()
                print("la liste des notes des étudiants est:",note)
            elif user=="b":
                moyenne=open("moyenne.txt","r")
                contenu=moyenne.read()
                print("la listes des Moyennes des étudiants est:",contenu)
            elif user=="c":
                for i in range (len(contenu2)):
                    maxnote=max(contenu2)
                    if maxnote==contenu2[i]:
                           print("la plus forte moyenne general")
                           print("le nom de cet eleve est:",nom2[i])
                           print("la note de devoir de cet eleve est:",note2[i])
                           print("la note d' Examen de cet  eleve est:",exam2[i])
                           print("la moyenne génerale de cet eleve est:",contenu2[i])
                for i in range (len(contenu2)):
                    minnote=min(contenu2)
                    if minnote==contenu2[i]:
                           print("la plus faible moyenne generale")
                           print("le nom de cet eleve est:",nom2[i])
                           print("la note de devoir de cet eleve est:",note2[i])
                           print("la note d' Examen de cet eleve est:",exam2[i])
                           print("la moyenne génerale de cet eleve est:",contenu2[i])
            elif user=="d":
                if econt=="":
                    print("le fichier est vide")
                else:
                    print(dcont)

            elif user=="e":
                if econt=="":
                    print("le fichier est vide")
                else:
                    print(econt)
            elif user=="f":
                if fcont=="":
                    print("le fichier est vide")
                else:
                    print(fcont)                             
            elif user=="g":
                print("n° \t Nom \tDevoir Surveillé \t Examen Final\t Moyenne Générale")
                for i in range (len(contenu2)):
                    print("{}\t{}\t{}\t{}\t{}".format(i+1,nom2[i],note2[i],exam2[i],contenu2[i]))


            elif user=="i":
                print("choisir\n\ta- ajouter une seule information\nb-ajout complet(nom,note devoir,exam,etc..")
                choix5=input("Que voulez vous ajouter?: ")
                if choix5=="a":
                    choix6=input("Quelle information voulez vous ajouter?")
                    if choix6=="nom":
                        newname=input("Quelle nom voulez vous ajouter?: ")
                        nom2.append(newname)
                        print("nom ajoutée")
                    elif choix6=="devoir":
                            newdev=float(input("Quelle note voulez vous ajouter?: "))
                            note2.append(newdev)
                            print("note ajoutée")
                    elif choix6=="exam":
                            newex=float(input("Quelle note d examen voulez vous ajouter?: "))
                            exam2.append(newex)
                            print("note  d examen ajoutée")    
                    elif choix6=="notetp":
                            tabtp=[]
                            for i in range (len(nom2)):
                                new=float(input("entrer 0"))
                                tabtp.append(new)
                            print("Voici les noms de vos eleves",nom2)
                            choix7=input("A quel éleve voulez vous ajouter cette information")
                            index=nom2.index(choix7)
                            newtp=float(input("entrer la note: "))
                            tabtp[index]=newtp
                            print("l information a bien été ajoutée a l elève")
                    elif choix6=="noteintero":
                            tabint=[]
                            for i in range (len(nom2)):
                                new=float(input("entrer  un null(0):   "))
                                tabint.append(new)
                            print("Voici les noms de vos eleves",nom2)
                            choix7=input("A quel éleve voulez vous ajouter cette information")
                            index=nom2.index(choix7)
                            newint=float(input("entrer la note: "))
                            tabint[index]=newint
                            print("l information a bien été ajoutée a l elève")




                elif choix5=="b":
                    nombre=len(exam2)
                    nombre2=int(input("entrer le nombre  d etudiants:  "))
                    nombre3=nombre+nombre2
                    while nombre2>0:
                        noms=input("entrer le nom de l etudiant:  ")
                        notedevoir=float(input("entrer la note devoir:  "))
                        noteexam=float(input("entrer la note examen: "))
                        moyenne=(notedevoir*0.4)+(noteexam*0.6)
                        nom2.append(noms)
                        note2.append(notedevoir)
                        exam2.append(noteexam)
                        contenu2.append(moyenne)
                        nombre2-=1
                        
                    print("n° \t Nom \tDevoir Surveillé \t Examen Final")
                    for i in range (nombre3):
                        print("{}\t{}\t{}\t{}\t{}".format(i+1,nom2[i],note2[i],exam2[i],contenu2[i]))
                    print("Les informations ont bien étés ajoutées")

                    
                
            elif user=="j":
                print("choisir\n\ta-une seule information\nb-informations completes(nom,note devoir,exam,etc..")
                choix5=input("Que voulez vous modifiez? ")
                if choix5=="a":
                    print("nom:modifier le nom\ndevoir:modifier la note de devoir\nexam:modifier la note d examen")
                    choix6=input("Quelle information voulez vous modifier")
                    if choix6=="nom" or choix6=="Nom":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("Quel nom voulez vous modifier ou remplacer? ")
                        newname=input("Veuillez entrer le nouveau Nom")
                        index=nom2.index(choix7)
                        nom2[index]=newname
                        print("nom modifié",nom2)
                    elif choix6=="devoir":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                        index=nom2.index(choix7)
                        newnoteds=float(input("Veuillez entrer la nouvelle note de devoir"))
                        note2[index]=newnoteds
                        print("Note de devoir  modifiée",note2)
                    elif choix6=="exam":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("la note d' examen de quel etudiant voulez vous modifier ou remplacer? ")
                        index=nom2.index(choix7)
                        newnoteexam=float(input("Veuillez entrer la nouvelle note d' examen"))
                        exam2[index]=newnoteexam
                        print("Note d' examen  modifiée",exam2)
                    elif choix6=="notetp":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                        index=nom2.index(choix7)
                        newnotetp=float(input("Veuillez entrer la nouvelle note de tp"))
                        tabtp[index]=newnotetp
                        print("Note de tp  modifiée",tabtp)
                    elif choix6=="interro":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("la note de devoir de quel etudiant voulez vous modifier ou remplacer? ")
                        index=nom2.index(choix7)
                        newnoteint=float(input("Veuillez entrer la nouvelle note de devoir"))
                        tabint[index]=newnoteint
                        print("Note d interro modifiée",tabint)
                elif choix5=="b":
                    choix6=input("entrer le nom de l etudiant dont vous voulez modifier les informations")
                    index=nom2.index(choix6)
                    newnoteds=float(input("entrer sa nouvelle note de devoir"))
                    newnoteexam=float(input("entrer sa nouvelle note d  Exam"))
                    note2[index]=newnoteds
                    exam2[index]=newnoteexam
                    print("les informations ont bien été modifieés")
            elif user=="k":
                print("choisir\n\ta- supprimer une seule information\n \tb-supprimer les informations completes(nom,note devoir,exam,etc..")
                choix5=input("Que voulez vous supprimer? ")
                if choix5=="a":
                    print("nom:supprimer le nom\ndevoir:supprimerla note de devoir\nexam:supprimer la note d examen")
                    choix6=input("Quelle information voulez vous supprimer")
                    if choix6=="nom" or choix6=="Nom":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("Quel nom voulez vous supprimer? ")
                        index=nom2.index(choix7)
                        del(nom2[index])
                        print("nom supprimé",nom2)
                    elif choix6=="devoir":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("la note de devoir de quel etudiant voulez vous supprimer? ")
                        index=nom2.index(choix7)
                        del(note2[index])
                        print("Note de devoir  supprimée",note2)
                    elif choix6=="exam":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("la note d' examen de quel etudiant voulez vous supprimer? ")
                        index=nom2.index(choix7)
                        del(exam2[index])
                        print("Note d' examen  supprimée",exam2)
                    elif choix6=="notetp":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("la note de devoir de quel etudiant voulez vous supprimer? ")
                        index=nom2.index(choix7)
                        del(tabtp[index])
                        print("Note de tp supprimée",tabtp)
                    elif choix6=="interro":
                        print("Voici les noms de vos eleves",nom2)
                        choix7=input("la note d' interrogation de quel etudiant voulez vous supprimer? ")
                        index=nom2.index(choix7)
                        del(tabint[index])
                        print("Note d interrogation supprimée",tabint)
                elif choix5=="b":
                    print("Voici les noms de vos eleves",nom2)
                    choix6=input("entrer le nom de l etudiant dont vous voulez supprimer les informations")
                    index=nom2.index(choix6)
                    del(nom2[index])
                    del(note2[index])
                    del(exam2[index])
                    print("les informations ont bien été supprimées")
                  
        elif choix2=="non":
            break
        
        
            
          
        
