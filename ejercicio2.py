valor1 = float(input("ingrese un valor: ")) 
valorr2 = float(input("ingresa otro valor: "))
if valor1 > valorr2:
    print(valor1, "es mayor que", valorr2)
elif valorr2 < valor1:
    print(valorr2, "es mayor que", valor1)
elif valor1 == valorr2:
    print("los numeros son iguales")