benimListem = [5,10,15,20,25,30]
for numara in benimListem:
    print(numara/5)

for numara in benimListem:
    if numara == 15:
        break
    print(numara)

for numara in benimListem:
    if numara == 15:
        continue
    print(numara)

for numara in benimListem:
    if numara == 15:
        pass
    #pass genelde ya orada bir işlem yapmayacaksak
    #ya da daha sonra orada bir işlem yapacaksak
    #ya da bir şey yazmazsak kod çalışmayacağı için yazıyoruz

