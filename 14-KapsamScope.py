number = 20
def multiplication(digit):
    number = 10
    return number * digit
print(multiplication(5))

print(number)

x=20
x=10

print(x)


## Local, Enclosing, Global,Built-In

myname = "Charlie"
#global
def myFonc():
    #myname = "Mahmut"
    #Enclosing
    def innerFonc():
        #myname = "Ayse"
        #local
        print(myname)
    print(innerFonc())
myFonc()
print(myname)    


y = 10

def yeniFonksiyon(y):
    print(y)
    y=5
    print(y)
    return y
print(yeniFonksiyon(3))

y = yeniFonksiyon(3)

print(y)

y=10
def ornekFonksiyon():
    global y
    y=5
    print(y)
ornekFonksiyon()
    
    
    