print(3 > 1)
if 3> 4:
    print("atıl samancıoğlu")
    print("if kosulu sağlandı")
print("if koşulunun dışına çıktık")
x=4
y=4
if x> y:
    print("x,y'den daha büyükmüş")
elif y > x:
    print("y, x'den daha büyükmüş")
#else if = elif (eğer öyle değil şöyleyse)
else:
    print("y ve x birbirine eşitmiş")

benimKahramanim = input("Super kahraman seçiniz:")
if benimKahramanim == "Batman":
    print("Batmani seçtiniz tebrikler")
elif benimKahramanim == "Superman":
    print("Keşke Batman'i seçseydiniz")
elif benimKahramanim== "Ironman":
    print("Ironman kimdir?")
else:
    print("bu kim gerçekten bilmiyoruz")
    
a=10
b=20
c=30
if a > b and b > c:
    print("a, b'den büyük VE b de c'den büyük")
elif a < b and b < c:
    print("a, b'den küçük Ve b de c'den küçük")
else: print("bu koşullar tutmadı")

m=10
k=4
l=1

if m>k or k>l:
    print("bu çalıştırılacak mı?")

karakterCanli = True
if karakterCanli == True:
    print("oyun karakteriniz yaşıyor")
else:
    print("oyun karakteriniz yaşamıyor")

if karakterCanli:
    print("oyun karakteriniz yaşıyor")
else: print("oyun karakteriniz yaşamıyor")
    
if not karakterCanli:
    print("karakter canlı değil")

benimString = "Atıl Samancıoğlu"
if benimString == "atıl Samancıoğlu":
    print("eşitmiş")
else:
    print("eşit değilmiş")

if "cıoğlu" in benimString:
    print("varmış")
else:
    print("yokmuş")

benimListem = [10,20,30,40,50]
if 10 in benimListem:
    print("evet var")


benimSozluk = {"muz" : 100, "elma": 150, "karpuz":500}
if "muz" in benimSozluk.keys():
    print("varmış")

if 500 in benimSozluk.values():
    print("varmış")
    