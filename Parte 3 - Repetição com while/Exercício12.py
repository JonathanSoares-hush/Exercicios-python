## Peça números ao usuário e vá somando. Quando ele digitar 0, pare e exiba a soma.

soma = 0 
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    soma += numero

print(f"A soma dos números digitados é: {soma}")