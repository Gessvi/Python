num1 = float(input("Insira o 1º numero: "))
num2 = float(input("Insira o 2º numero: "))
pergunta = input("Escolha um operador:  + | - | / | * :  ")

operador = pergunta

match  operador:
    case "+":
        resultado = num1 + num2
        print(resultado)
    case "-":
        resultado = num1 - num2
        print(resultado)
    case "*":
        resultado = num1 * num2
        print(resultado)
    case "/":
        resultado = num1 / num2
        print(resultado)