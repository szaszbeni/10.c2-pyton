from random import *

def listaAlapok():
    #lista létrehozása
    alapok=[]
    for i in range(10):
        alapok.append(randint(1,10))
    alapok.append("alma")
    alapok.append("szilva")
    print(alapok)
    #lista kiírása szépen
    for item in alapok:
        print(item, end=" ")
    print()
    print(alapok[4]) # 4es indexü elem (sorban az 5dik)
    print(len(alapok)) #lista elemszáma
    alapok.insert(4,"körte") # elem beszúrása adott helyre
    for item in alapok:
        print(item, end=" ")
    print()
    print(alapok.index("körte")) #elem indexe
    #print(alapok.index(55)) #hiba üzenet mert nincs benne
    alapok.remove("körte") #törlése
    alapok.pop() #utolsó törlése
    del alapok[-1] #elsö törlése
    del alapok[1] #1es törlése
    #alapok.clear() lista elemeket törli
    #del alapok  a teljes listát törli
    alapok.reverse() #megfordítja
    alapok.sort() #növekvő sorrend
    alapok.reverse()
    print()
    print(alapok[5:]) #5ös indextöl a végéig
    print(alapok[:4]) #az elejétől az adott indexüig
    print(alapok[-1]) #utolsó
    print(alapok[-2]) #utolsó elötti
    print(alapok[-2:]) #utolsó 2
    print(alapok[3:5])
    alapok[6]="narancs"
    print(alapok[6])
    print()
    for item in alapok:
        print(item, end=" ")
    print()


def feladat1():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) #ellenörzés miatt
    paratlandb=0
    for item in szamok:
        if item%2==1:
            paratlandb+=1
    print("A páratlanok száma",paratlandb)

def feladat2():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) #ellenörzés miatt
    osszeg=0
    for item in range(elemszam):
        if item%2==0:
            osszeg=item
    print("A párosak száma",osszeg)

def feladat3():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) #ellenörzés miatt
    for i in range(len(szamok)):
        if szamok[i]%2==0:
            print(i, "t", szamok[i])

#listaAlapok()
#feladat1()
#feladat2()
feladat3()