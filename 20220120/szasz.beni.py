from math import *

def feladat1():
    szamok=[]
    a=int(input("Add meg a számok számát:"))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot:")))
    print(szamok)
    db=0
    for item in szamok:
        if item%2==1:
            db=db+1
    if db>0:
        print("A páratlanok darabszáma:",db)
    else:
        print("Nincsenek páratlan számok.")


def feladat2():
    szamok=[]
    ossz=[]
    a=int(input("Agy meg egy számot:"))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot:")))
    print(szamok)
    db=0
    for item in szamok:
        if item*2==1:
            db=db+1
    if db>0:
        print("A páros számok:",db)
    else:
        print("Nincs páros szám.")
    print("Összege:",sum(ossz),"db")

#feladat1()
feladat2()
