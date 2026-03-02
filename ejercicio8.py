import random
x = 0
y = 0

print("tu posision inicial es X=0 , Y=0")
print("se lanza el dado 10 veces")

for i in range(10):
    numero = random.randint(1, 4)
    print(numero)
    if numero == 1:
        x = x+1
    elif numero == 2:
        y = y-1
    elif numero == 3:
        x = x-1
    elif numero == 4:
        y = y+1
        
print("tu posicion final es: ")
print("posicion en X: ", x)
print("posicion en Y", y)
