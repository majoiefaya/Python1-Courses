r1=int(input("entrer la valeure de R1:"))#r1=resistance 1
r2=int(input("entrer la valeure de R2:"))#r2=resistance 2
r3=int(input("entrer la valeure de R3:"))#r3=resistance 3
rser=r1+r2+r3#rser=resistance equivalente en serie
rpar=(r1*r2*r3)/((r1*r2)+(r1*r3)+(r2*r3))#rpar=resistance equivalente en parallèle
print("en serie la resistance equivalente est:",rser)
print("en paralèlle la resistance equivalente est:",rpar)