class Vercsoport:
    def __init__(self, egysor):#kezdo ertekek beallitasa konstruktor
        darabok=egysor.strip().split(" ")
        self.vercs=darabok[0]
        self.rh=darabok[1]

def cipo():
    f=open("cipomeret.txt", "r")
    sor=f.readline()
    print(sor)
    f.close()
    meretek=sor.strip().split(" ")
    # A strip levagja a szokozeket az elejerol es a vegerol.A split feldarabolja a szokoz menten.
    print(meretek)
    meret=[]
    for item in meretek:
        meret.append(int(item))
    print("db", len(meret))
    print("min:", min(meret))
    print("max:", max(meret))
    print("összeg:", sum(meret))
    print("átlag:", sum(meret)/len(meret))


def primek12ig():
    f=open("primek12ig.txt", "r")
    alma=[]
    while True:
        sor=f.readline()
        if len(sor)==0:
            break
        else:
            alma.append(int(sor))
    f.close
    for item in alma:
        print(item, end=" ")
    
    f=open("primek12ig.txt","r")
    listam=f.readlines()
    korte=[]
    for item in listam:
        korte.append(int(item))
    print(korte)
    f.close

def vercsoport():
    f=open("vercsoportok.txt","r")
    beolvas=f.readlines()
    f.close()
    vercsoportok=[]
    for item in beolvas:
        vercsoportok.append(Vercsoport(item))
    print(vercsoportok[0].rh)
    db_ab=0
    for item in vercsoportok:
        if item.vercs.lower()=="ab":
            db_ab+=1
    print("Az ab vércsoportnak száma:",db_ab)
    db_min=0
    for item in vercsoportok:
        if item.rh=="-":
            db_min+=1
    print("A - vércsoportnak száma:",db_min)
    db_plus=0
    for item in vercsoportok:
        if item.rh=="+":
            db_plus+=1
    print("A + vércsoportnak száma:",db_plus)
    db_a=0
    for item in vercsoportok:
        if item.vercs.lower()=="a":
            db_a+=1
    print("Az a vércsoportnak száma:",db_a)
    db_b=0
    for item in vercsoportok:
        if item.vercs.lower()=="b":
            db_b+=1
    print("Az b vércsoportnak száma:",db_b)
    print("Az összes vércsoport:",len(vercsoportok))
    db_0neg=0
    for item in vercsoportok:
        if item.vercs=="0" and item.rh=="-":
            db_0neg+=1
    print("A 0- vércsoportuak száma:",db_0neg)
    f=open("vercsoportok.txt","r")
    sor=f.read()
    print("Máshogy 0 -:", sor.count("0 -"))
    f.close()
    


#cipo()
#primek12ig()
#vercsoport()