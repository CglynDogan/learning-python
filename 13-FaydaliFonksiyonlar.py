


def bolmeIslemi(numara):
    return numara /2

print(bolmeIslemi(20))
    
benimListem=[1,2,3,4,5,6,7,8,9,10]

yeniListe = []
for eleman in benimListem:
    yeniListe.append(bolmeIslemi(eleman))
    print(yeniListe)


## Map fonskisyonu haritalamak anlamına geliyor 

print(list(map(bolmeIslemi,benimListem)))


def kontrolFonksiyonu(string):
    return "a" in string

print(kontrolFonksiyonu("atıl"))
print(kontrolFonksiyonu("zeynep"))

stringListesi = ["atıl", "samancıoğlu", "atlas","zeynep", "mehmet", "ahmet","levent"]
print(list(map(kontrolFonksiyonu,stringListesi)))
sonucListesi = list(map(kontrolFonksiyonu,stringListesi))
print(sonucListesi.count(False))

##filter 

print(list(filter(kontrolFonksiyonu,stringListesi)))


##lambda 

multiplication = lambda number : number *3
print(multiplication(10))

exampleList = [10,20,30]

print(list(map(lambda number : number *4, exampleList)))