benimAdım = "Çağlayan Doğan"
print(benimAdım.upper())
print(benimAdım)

benimAdımBuyukHarfli = benimAdım.upper()
print(benimAdımBuyukHarfli)

print(benimAdım)

def ilkFonksiyon():
    print("ilk fonksiyonum")

print(ilkFonksiyon())
    

#input & return

def merhabaDunya(yazdirilacakIsım):
    print("merhaba")
    print(yazdirilacakIsım)

print(merhabaDunya("python"))

def merhaba(isim= "atıl"):
    print("merhaba")
    print(isim)
print(merhaba("python"))


def toplama(numara1, numara2):
    sonuc = numara1 + numara2
    print(sonuc)
print(toplama(10,20))

print(toplama(-200,350))

def superToplama(num1,num2,num3):
    print(num1+num2+num3)
print(superToplama(10,20,30))
    

yeniDegisken = toplama(10,20)

print(type(yeniDegisken))

def dondurmeliToplama(num1,num2):
    return num1+num2
yeniSonuc = dondurmeliToplama(10,20)

print(type(yeniSonuc))

def kontrolFonksiyon(s):
    if s == "çağlayan":
        print("verdiğiniz string çağlayan")
    else:
        print("verdiğiniz string başka bir şey")
print(kontrolFonksiyon("çağlayan"))
print(kontrolFonksiyon("python"))
## args & kwargs
# argümanlar ve keywords argümanlar
#önündeki yıldız istediğin kadar koyabileceğin anlamına geliyor
def yeniToplama(*args):
    return sum(args)

print(yeniToplama(10,20,30,40,50,60))
print(yeniToplama(10,20,30))

def benimFonksiyonum(*args):
    return(args)

print(type(benimFonksiyonum(20,30,40)))

def ornekFonksiyon(**kwargs):
    return(kwargs)

print(type(ornekFonksiyon(muz = 100, elma= 200, ananas=300)))

def keyWordKontrolu(**kwargs):
    if "atıl" in kwargs:
        print("atıl var")
    else:
        print("atıl yok")
print(keyWordKontrolu(atıl= 70,zeynep= 50, mehmet= 40))
    


    


    
    