print ("----- BEM VINDO AO CASSINO G88433 -----")
print ("---- A turma da jogatina! ----")
print ("Gerando numeros aleatórios...")
time.sleep(5)
lista = []
x = 0
while x < 5:
    numero = random.randint(1,100)
    lista.append(numero)
    x += 1
#print (lista)
print ("Numeros gerados! ")
chances = 23
time.sleep(3)
print ("Iniciando o jogo...")
while chances != 0:
    time.sleep(1)
    num = int (input("Digite um numero: "))
    if num in lista:
        print ("Parabéns você acertou!")
        break
    else:
        print ("Errou!Tente novamente!")
        chances -= 1
        print (f"Você tem {chances} chances")
print ("Os numeros sorteados foram: ")
print(lista)