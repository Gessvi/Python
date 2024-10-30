lados = []

for i in range(3):
    lado = float(input(f"Digite o comprimento do lado {i + 1}: "))
    lados.append(lado)


if lados[0] + lados[1] > lados[2] and lados[0] + lados[2] > lados[1] and lados[1] + lados[2] > lados[0]:
    print("É possível formar um triângulo.")
    
    if lados[0] == lados[1] == lados[2]:
        print("Tipo: Equilátero")
    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        print("Tipo: Isósceles")
    else:
        print("Tipo: Escaleno")
else:
    print("Não é possível formar um triângulo.")