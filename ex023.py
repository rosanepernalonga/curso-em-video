# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade: ', u)
print('A dezena:  ', d)
print('A centena: ', c)
print('O milhar:  ', m)