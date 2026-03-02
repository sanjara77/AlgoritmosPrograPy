print("vota por tu candidato favorito")
print("1. Candidato A")
print("2. Candidato N")
print("3. Candidato M")

candidato = input("ingresatu voto: ")

if candidato == "A":
    print("Has votado por el partido Amarillo")
elif candidato == "N":
    print("Has votado por el partido Naranja")
elif candidato == "M":
    print("Has votado por el partido Morado")
else:
    print("Candidato invalido")
