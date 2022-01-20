benimListem = [0,1,2,3,4,5,6]
for numara in benimListem:
    print(numara)

##Range (kapsam veya bir yerden bir yere giderken ki
# genişlik)

print(range(15))
print(list(range(20)))

for numara in list(range(15)):
    print(numara*5)


print(list(range(5,22,4)))


## enumerate

index = 0
for numara in list(range(5,15)):
    print(f"güncel numara: {numara} güncel index: {index}")
    index = index + 1

#for eleman in enumerate(list(range(5,15))):
    #print(type(eleman))
    #print(eleman)


for (index,numara) in enumerate(list(range(5,15))):
    print(index)
    print(numara)

##random 


    