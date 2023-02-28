import array as lim
tabnoms=[]
tabnotedevoir=lim.array('d',[])
tabnoteexam=lim.array('d',[])
tabmoyenne=lim.array('d',[])
nombre=int(input("entrer le nombre d eleves"))
while nombre>0:
    nombre-=1
    nom=str(input("entrer le nom"))
    notedevoir=float(input("entrer la note devoir"))
    noteexam=float(input("entrer la note examen"))
    moyenne=(notedevoir*0.4)+(noteexam*0.6)
    tabnotedevoir.append(notedevoir)
    tabnoteexam.append(noteexam)
    tabmoyenne.append(moyenne)
    tabnoms.append(nom)
print("noms:",tabnoms)
print("note:",tabnotedevoir)
print("exam:",tabnoteexam)
print("moy:",tabmoyenne)


