#calcule a soma entre todos os números ímpares, multiplos de 3 no intervalo de 1 a 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos {} os valores é: {}'.format(cont, soma))
