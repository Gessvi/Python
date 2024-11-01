ganha = float(input("Quanto voce ganha por hora? "))
horas = int(input("Quantas horas trabalhadas? "))
dias = 30

bruto = ganha * horas * dias
imposto = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - (imposto + inss + sindicato)

print("Salario Bruto: ", bruto)
print("Salario imposto: ", imposto)
print("Pago ao INSS: ", inss)
print("Pago ao Sindicato: ", sindicato)
print("Salario liquido: ", liquido)
