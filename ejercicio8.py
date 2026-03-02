x = 0
y = 0

print("Tu posición inicial es X=0, Y=0")
print("Ingresa 10 números entre 1 y 4")

contador = 0

while contador < 10:
    numero = int(input("Lanzamiento: "))

    if numero == 1:
        x = x + 1
    elif numero == 2:
        y = y - 1
    elif numero == 3:
        x = x - 1
    elif numero == 4:
        y = y + 1
    else:
        print("Número inválido")

    contador = contador + 1

print("Tu posición final es:")
print("Posición en X:", x)
print("Posición en Y:", y)
