#elágazás
def feladat1(szam):
    if szam<16:
        print("A szám tízszerese:",szam*10)
    else:
        print("A szám harmada:",round(szam/3,2))

def feladat2(szam):
    if szam%2==0:
        print("A szám páros!")
    else:
        print("A szám páratlan!")

def feladat3(szam):
    if 10<szam<50:
        if szam//10==1:
            print("tizesek")
        elif szam//10==2:
            print("huszasok")
        elif szam//10==3:
            print("harmincasok")
        elif szam//10==4:
            print("negyvenesek")
    else:
        print("A szám nem esik 10 és 50 közé!")

def feladat4(szam):
    if 12<szam<25:
        if szam%2==0:
            print("A szám páros!")
        else:
            print("A szám páratlan!")
    else:
        print("Aszám nem esik 12 és 25 közé!")
 
#ciklus    
def feladatc1():
    for i in range(1,18):
        print(i*3,end=" ")

def feladatc2():
    for i in range(1,17):
        print(pow(2,i),end=" ")

def feladatc3():
    for i in range(1,6):
        for o in range(1,16):
            print(i*o,end=" ")
        print()

def feladatc4():
    for i in range(1,26):
        if i*7%4==0:
            print(i*7,end=" ")

def feladatc5():
    a=2
    b=3
    c=5
    print("a=",a,"b=",b,"c=",c,"V=",a*b*c)
    for i in range(1,5):
        a=a+1
        b=b+2
        c=c+3
        print("a=",a,"b=",b,"c=",c,"V=",a*b*c)

def feladatc6():
    for i in range(15,93):
        print(i,end=" ")

def feladatc7():
    for i in range(100,401):
        print(i/4,end=" ")


# itt kezdodik
#szam=int(input("Kérek egy egész számot: "))
#feladat1(szam)
#feladat2(szam)
#feladat3(szam)
#feladat4(szam)

#feladatc1()
#feladatc2()
#feladatc3()
#feladatc4()
#feladatc5()
#feladatc6()
#feladatc7()