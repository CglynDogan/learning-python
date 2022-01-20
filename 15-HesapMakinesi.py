def hesapla(a,b,islem):
    if islem not in "+-*":
        return "Lütfen su islemlerden birini seçiniz: +-*/"
    
    if islem == "+":
        return (str(a)+" + "+str(b) + " = " +str(a+b))
    if islem == "-":
        return (str(a)+" - "+str(b) + " = " +str(a-b))
    if islem == "*":
        return (str(a)+" * "+str(b) + " = " +str(a*b))
    if islem == "/":
        return (str(a)+" / "+str(b) + " = " +str(a/b))
while True:
    try: 
        a= int(input("ilk sayıyı giriniz:"))
        b= int(input("ikinci sayıyı giriniz:"))
        islem = input("isleminizi seciniz: +-*/")
        print(hesapla(a,b,islem))
    except:
        print("Lütfen sayıları düzgün giriniz")


