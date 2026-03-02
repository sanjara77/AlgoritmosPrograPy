num1 = float(input("ingresa un numero: "))
num2 = float(input("ingresa un segundo numero: "))

print("que operacion desea realizar?")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")

operacion = input("selecciona una operacion presionando el numero correspondiente: ")

if operacion == "1":
    resultado = num1 + num2
    print(resultado)
elif operacion == "2":
    resultado = num1 - num2
    print(resultado)
elif operacion == "3":
    resultado = num1 * num2
    print(resultado)
elif operacion == "4":
    if num2 == 0:
        print("error de calculo")
    else:
        resultado = num1 / num2
        print(resultado)
