benimListem = [1,2,3]
print (benimListem[0])

benimYemeklerim = ["Elma", "Karpuz", "Muz"]
print(benimYemeklerim)
benimKalorilerim= [100,200,300]
print(benimYemeklerim[1])
print(benimKalorilerim[1])

#dictionary
benimSozluk={"anaharkelime": "deger"}
print(benimSozluk)
type(benimSozluk)
print(benimSozluk["anaharkelime"])
benimYemekKaloriSozlugum ={"elma": 100, "karpuz": 200, "muz": 300}
print(benimYemekKaloriSozlugum)
print(benimYemekKaloriSozlugum["muz"])
benimYemekKaloriSozlugum["elma"] = 200
print(benimYemekKaloriSozlugum)
benimDegisikSozlugum = {1:"atıl", 2:"atlas"}
print(benimDegisikSozlugum[1])
print(benimDegisikSozlugum[2])

yeniDictionary= {"anahtar1" : 100, "anahtar2" : [10,20,30,40,4.5,"atıl"], "anahtar3": {"anahtar9":4}}
print(yeniDictionary)
print(yeniDictionary.keys())
print(yeniDictionary.values())
print(yeniDictionary["anahtar2"][-1])
print(yeniDictionary["anahtar3"]["anahtar9"])
