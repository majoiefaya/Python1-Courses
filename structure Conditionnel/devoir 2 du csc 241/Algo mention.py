note_1=int(input("entrer la premiere note: "))#coef=coefficient
coef_1=int(input("entrer le coefficient de la 1ere note: "))
note_2=int(input("entrer la 2eme note: "))
coef_2=int(input("entrer le coefficient de la 2eme note: "))
note_3=int(input("entrer la 3eme note: "))
coef_3=int(input("entrer le coefficient de la 3eme note: "))
moyenne=((note_1*coef_1)+(note_2*coef_2)+(note_3*coef_3))/(coef_1+coef_2+coef_3)
if moyenne>=18:
    print("EXCELLENT")
elif moyenne>=16 and moyenne<18:
    print("TRES BIEN")
elif moyenne>=14 and moyenne<16:
    print("BIEN")
elif moyenne>=12 and moyenne<14:
    print("ASSEZ-BIEN")
elif moyenne>=10 and moyenne<12:
    print("PASSABLE")
else:
    print("INSUFFISANT")