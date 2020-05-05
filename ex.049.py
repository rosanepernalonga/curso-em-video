#refaça o desafio 9 da tabuada
n = int(input('Digite um número para ver sua tabuada: '))
for t in range(1,11):
    print('{} x {} = {}'.format(n, t, t*n))