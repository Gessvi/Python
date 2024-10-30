pergunta = input("Voce abasteceu com Alcool ou Gasolina? ")
gasolina = 6.50
alcool = 5.00

if (pergunta == "gasolina"):
    print(gasolina)
else:
    desconto = (alcool * 0.5) - alcool
    print(desconto)