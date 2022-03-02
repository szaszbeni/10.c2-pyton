from random import *

def feladat1():
    a = input("Kérek egy szöveget!")
    szavak = a.split()
    print("A szöveg",len(szavak),"szóbol áll.")
    print("A szöveg",len(a),"karakterből áll." )
    b = a.count("e")
    print("A szövegben",b,"e betű van.")

def feladat2():
    for i in range(-20,21):
        print(i,end=" ")
        if 3/==i:
            print("Hárommal oszthatók:",i)
        else:
            print("Hárommal nem oszthatók",i)


#feladat1()
feladat2() #nem jó