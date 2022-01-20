x = 0
while x < 10:
    print(x)
    x= x +1

benimListem= [1,2,3,4,5]
print(benimListem.pop())   #pop son elemanı çıkartıyor
print(benimListem.append(5)) #append ekliyor
print(benimListem)
while 3 in benimListem:
    print("3 hala listenin içerisinde")
    benimListem.pop()

numara = 0
while numara < 5:
    if numara == 4:
        break
    print(numara)
    numara = numara + 1

yeniDegisken = 0
while yeniDegisken < 15:
    print(f"yeniDegisken'in güncel degeri: {yeniDegisken}") #f format anlamına geliyor
    # süslü parantez içerisinde yazılan şeyleri kod olarak algılamasını sağlıyor
    yeniDegisken = yeniDegisken +1
    