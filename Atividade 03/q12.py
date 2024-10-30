peso = float(input("Insira seu Peso: "))

if (peso < 57):
    print("Abaixo do Peso")
elif (peso >= 57 and peso < 74):  
    print("Peso Normal")
elif (peso >= 74 and peso < 90):
    print("Sobrepeso")
else:
    print("Obesidade")
