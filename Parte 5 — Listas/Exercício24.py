## Dada a lista [5, 12, 8, 20, 3, 15], informe quantos itens são maiores que 10.

numeros = [5, 12, 8, 20, 3, 15]
maiores_que_10 = [n for n in numeros if n > 10]
print(len(maiores_que_10), "numeros são maiores que 10.")