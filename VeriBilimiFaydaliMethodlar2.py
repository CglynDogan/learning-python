from random import randint, shuffle
print(randint(0,100))

yeniListe = list(range(0,10))
print(yeniListe)

shuffle(yeniListe)
print(yeniListe)


#### zip ####

yemekListesi= ["muz", "ananas", "elma"]
kaloriListesi = [100,200,300]
gunListesi = ["pazartesi", "salı", "çarşamba"]

#print(type(zip(yemekListesi,kaloriListesi,gunListesi)))
ziplenmisListe =list(zip(yemekListesi,kaloriListesi,gunListesi))
for eleman in ziplenmisListe:
    print(type(eleman))


#listeler ileri seviye

#listeOrnegi =[]
#benimString = "Çağlayan Doğan"

#for harf in benimString:
 #   listeOrnegi.append(harf)
#print(listeOrnegi)

#iki kodda aynı işlemi görüyor hangisini kullanmak istersen.

yeniString = "çağlayan doğan"
yeniListeOrnegi = [eleman for eleman in yeniString]
print(yeniListeOrnegi)

ikinciListeOrnegi = [numara**5 for numara in list(range(0,10))]
print(ikinciListeOrnegi)