#leia 6 numeros inteiros, mostre a soma dos numeros pares
soma = 0
for n in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares digitados é: {}'.format(soma))