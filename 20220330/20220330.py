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
        

#cipo()
primek12ig()