n=int(input("entrer un nombre compris entre 10 et 20:  "))
while n<10 or n>20:
    n=int(input("Veuillez resaisir:  "))
    if n<10 or n>20:
        print(n,"n' est pas compris entre 10 et 20.veuillez resaisir.")
    if n<10:
        print("Plus grand!")
    elif n>20:
        print("Plus petit!")
    
    
    