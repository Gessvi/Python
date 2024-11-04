list = [22,32,55,33,66,99,88]
chances = 10
while chances != 0:
    num = int (input("Insira umnumero: "))
    if num in list:
        print("Parabnes voce acertou")
        break
else:
    print("Errou!Tente Novamente!")
    chance += 1
