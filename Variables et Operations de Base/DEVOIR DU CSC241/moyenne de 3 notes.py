note_1=int(input("entrer la premiere note:"))
coef_1=int(input("entrer le coefficient du 1er nombre:"))
note_2=int(input("entrer la 2eme note:"))
coef_2=int(input("entrer le coefficient de la 2eme note:"))
note_3=int(input("entrer la 3eme note:"))
coef_3=int(input("entrer le coefficient de la 3eme note:"))
moyenne=((note_1*coef_1)+(note_2*coef_2)+(note_3*coef_3))/(coef_1+coef_2+coef_3)
print("la moyenne des trois note est:",moyenne)