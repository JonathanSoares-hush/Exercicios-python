## Peça a média de um estudante e classifique: 6 ou mais é Aprovado; de 4 a 5,9 é Recuperação; abaixo de 4 é reprovado.

media = float(input("Digite a média do estudante: "))
if media >= 6:
    print("O estudante está Aprovado.")
elif media >= 4:
    print("O estudante está em Recuperação.")
else:
    print("O estudante está Reprovado.")
