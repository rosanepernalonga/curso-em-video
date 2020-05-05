#leia um numero inteiro e diga se ele é ou não um número primo
num = int(input('Digite um número inteiro: '))
if num % num == 0 and num % 2 != 0 and num % 3 != 0:
    print('O número {} é um número primo'.format(num))
else:
    print('O número {} NÃO é um número primo'.format(num))