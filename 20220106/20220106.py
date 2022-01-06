from math import *
from random import *

def feladat31():
    for i in range(10,101):
        if i%7==3:
            print(i ,end=" ")
    print()

def feladat3233():
    szovegeslista=[]
    szovegeslista=['alma', 'körte', 'szilva']
    szovegeslista.append('sárgabarack')
    szovegeslista.append('eper')
    print(szovegeslista)
    for item in szovegeslista:
        print(item, end=" ")
    print()

def feladat3435():
    karakterek=[]
    karakterek=["a", "b", "2", "@", "/"]
    print(type(karakterek[2]))

def feladat3637():
    egeszek=[2,5,45,6,-9]
    for item in egeszek:
        print(item, end=" ")
    print()

def feladat3839():
    valaszok=[0.2, 34.25, round(pi,2)]
    for item in valaszok:
        print(item, end=" ")
    print()

def feladat40():
    veletlenek=[]
    for i in range(15):
        veletlenek.append(randint(10,50))
    for item in veletlenek:
        print(item, end=" ")
    print()
    print('lagnagyobb:', max(veletlenek))
    print('legkissebb:', min(veletlenek))
    print('összes:', sum(veletlenek))
    print('átlaga:', sum(veletlenek)/len(veletlenek))
    print('terjedelme:', max(veletlenek)-min(veletlenek))
    if veletlenek*2:
        print(i, end=" ")
    



feladat31()
feladat3233() 
feladat3435() 
feladat3637()
feladat3839()
feladat40() 