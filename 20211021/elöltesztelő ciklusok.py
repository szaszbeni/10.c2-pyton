def feladat24():
    szam=float(input("Kérek egy számot!"))
    while szam!=0:
        szam=float(input("Kérek egy számot!"))


def feladat25():
    szam=float(input("Kérek egy pozitív számot!"))
    while szam<=0:
        szam=float(input("Nem pozitív számot adtál, add meg ujra!"))



def feladat26():
    szam=float(input("Kérek egy számot amely kissebb mint tíz!"))
    while szam<10:
        oszeg+=szam
    print("Számok összege",oszeg)

#feladat24()
#feladat25()
feladat26()