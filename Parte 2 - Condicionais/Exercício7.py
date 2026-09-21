## Peça dois números e exiba qual é o maior. Se forem iguais, informe isso.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior número é: " + str(numero1))
elif numero2 > numero1:
    print("O maior número é: " + str(numero2))
else:
    print("Os números são iguais.")
    