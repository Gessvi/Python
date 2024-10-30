preco = float(input("Qual é o preço? "))

if (preco > 100):
    desconto = (preco * 0.10)  - preco
    print(desconto)
else:
    print(preco)
