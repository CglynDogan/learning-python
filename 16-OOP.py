benimlistem= list()
print(type(benimlistem))

###############################################################
### instance & attributes

superKahramanAdi= "superman"
superKahramanYasi = 30
superKahramanMeslegi = "gazeteci"
ikincisuperkahramanadi="batman"

class SuperKahraman():
    
    ozelGuc= "Gorunmezlik"
    def __init__(self,isimInput,yasInput,meslekInput):
        print("init çağırıldı")
        self.isimInput = isimInput
        self.yasInput = yasInput
        self.meslekInput = meslekInput
    def ornekMethod(self):
        print(f"ben superkahramanım ve meslegim:{self.meslekInput}")
        
superman = SuperKahraman("Superman",30,"Gazeteci")
batman = SuperKahraman("Batman",45,"zengin")

superman.isim="Clark Kent"
print(superman.isim)
print(superman.yasInput)

superman.ozelGuc="Uçabiliyor"
print(superman.ozelGuc)
superman.ornekMethod()


class Kopek():
    
    yilCarpani= 7
    
    def __init__(self,yas=5):
        self.yas = yas
    def insanYasiniHesapla(self):
        return self.yas * self.yilCarpani
    
benimKopek = Kopek()
print(benimKopek.insanYasiniHesapla())


### inheritance

class Hayvan():
    def __init__(self):
        print("hayvan sınıfı init çağrıldı")
    def method1(self):
        print("hayvan sınıfı method1 çağrıldı")
    def method2(self):
        print("hayvan sınıfı method2 çağrıldı")
    def miyavla(self):
        print("miyav")
        
benimHayvanim = Hayvan()
benimHayvanim.method1()
benimHayvanim.method2()

class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("kedi sınıfı çağrıldı")
        
benimKedi= Kedi()
benimKedi.method1()
benimKedi.miyavla()


################################################################
### Polymorphism

class Elma():
    def __init__(self,isim):
        self.isim = isim
    def bilgiVer(self):
        return self.isim+ "100 kaloridir "

class Muz():
    def __init__(self, isim):
        self.isim = isim
    def bilgiVer(self):
        return self.isim+ "150 kaloridir "

elma= Elma("elma")
print(elma.bilgiVer())
muz = Muz("muz")
print(muz.bilgiVer())

meyveListesi = [elma,muz]
for meyve in meyveListesi:
    print(meyve.bilgiVer())
    
def bilgiAl(meyve):
    print(meyve.bilgiVer())
bilgiAl(muz)
bilgiAl(elma)
         
