peso = float(input("Insira o Peso do Peixe: "))

if (peso >= 50):
    excesso = peso - 50
    multa = excesso * 4

    print("Peso do peixe:", peso)
    print("Quantidade do peso adicional: ", excesso)
    print("Valor da multa: ", multa)
else:
   print("Peso Normal por Lei: ", peso)


#===== RESPOSTA 02 =====

#peso = float(input("Insira o Peso do Peixe: "))
#limite = 50
#taxa = 4

#if (peso >= 50):
#    excesso = peso - limite
#    multa = excesso * taxa

#    print("Peso do peixe:", peso)
#    print("Quantidade do peso adicional: ", excesso)
#    print("Valor da multa: ", multa)
#else:
#   print("Peso Normal por Lei: ", peso)