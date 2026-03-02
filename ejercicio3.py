hora = int(input("que hora es?: "))
if hora == 6:
    print("sonar alarma")
    respuesta = input("quieres detener la alarma?: (si o no): ")
    if respuesta == "si":
        print("la alarma se detuvo :)")
    elif respuesta == "no":
        print("la alarma se detendra en 60 segundos")
else:
    print("no sono la alarma")