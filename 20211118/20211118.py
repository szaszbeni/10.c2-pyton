def megtalal(karakterlanc, keresendo):
    if keresendo in karakterlanc:
        karakterlanc.index(keresendo)
    else:
        return -1

def karakterszam(karakterlanc, megszamolando):
    return karakterlanc.count(megszamolando)

def feladat2():
    szöveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus, similique!'
    karakter=input('Adj meg egy karaktert!')
    print(megtalal(szöveg, karakter))
    eredmeny=megtalal(szöveg, karakter)
    if eredmeny-1:
        print('A megadott karakter nem szerepel a szövegben!')
    else:
        print('Az eredmény pozíciói helyen fordul elő először!')

def feladat4():
    szöveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus, similique!'
    karakter=input('Adj meg egy karaktert!')
    karakterszam(szöveg, karakter)
    print('A megadott szövegben az adott karakter', karakterszam(szöveg, karakter) 'fordul elö')

def feladat5():
    szoveg:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus, similique!'
    print('A megadott szöveg', karakterszam(szoveg, ' ')+1 'szóbol áll')

def feladat6():
    prefixes=['ack']
    suffixe['J','K','L','L','M','N','O','P','Q']
    nevek[]

####HF 7,8,10


#Itt kezdödik a feladat!
#feladat2()
#feladat4()
#feladat5()
#feladat6()