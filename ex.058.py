#refaça o ex 028. dessa vez fazendo o usuário tentar até acertar.
#Escreva um programa que escolha aleatóriamente um número. Peça para o user tentar adivinhar até acertar
from random import randint
computador = randint(0,5)
palpite = int(input("Qual número você acha que eu escolhi? "))
while palpite != computador:
    palpite = input('Errou. Tente outra vez: ')
    if palpite == computador:
        print('Eu escolhi {} e você acertou!'.format(computador))
print('Parabéns!')
