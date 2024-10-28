idade = int(input("Insira sua idade: "))

if(idade < 18):
    print("Menor de idade")
elif(idade >= 18 and idade <= 60):
    print ("Adulto Assalariado")
else:
    print("Idoso")