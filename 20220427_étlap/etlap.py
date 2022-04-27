class Etel:
    def __init__(self,egysor):
        darabok=egysor.strip('\n').split('\t')
        self.nev=darabok[0]
        self.ar=int(darabok[1])
        self.tipus=darabok[2]

f=open('etelek.txt','r')
beolvas=f.readlines()
f.close
etelek=[]
for item in beolvas:
    etelek.append(Etel(item))
print(etelek[0].nev)
print(etelek[0].ar)
print(etelek[0].tipus)

print('2. feladat:Az étteremben',len(etelek),'féle étel van')
osszeg_leves=0
db_leves=0
for item in etelek:
    if item.tipus.lower()=='leves':
        osszeg_leves=osszeg_leves+item.ar
        db_leves+=1
print('A leves átlagosan',osszeg_leves,'forintba kerülnek.')
