from random import *

def feladat1():
    f=open("elsöirás.txt", "w", encoding="utf8")
    f.write("alma"+"/n")
    f.writelines("körte/r")
    f.writelines("szilva")
    f.close()

def feladat2():
    f=open("szamoktizig.txt", "w")
    for i in range(1,11):
        if i<10:
            f.write(str(i)+", ")
        else:
            f.write(str(i))
    f.close()


def feladat3():
    f=open("szamokegymasalatt.txt", "w")
    for i in range(1,11):
        if i<10:
            f.write(str(i)+"/r")
        else:
            f.write(str(i))
    f.close()

def feladat4():
    f=open("elsotiznegyzetszam.txt", "w")
    for i in range(1,11):
        if i<10:
            f.write(str(i*i)+", ")
        else:
            f.write(str(i))
    f.close()

def feladat5():
    f=open("veletlenszamok.txt", "w")
    for i in range(100,201):
        if i:
            f.write(str(i)+", ")
        else:
            f.write(str(i))
    f.close()


#feladat1()
#feladat2()
#feladat3() #müködik de rosszul
#feladat4()
feladat5() #nem jó