#Escreva um programa que escolha aleatóriamente um número. Peça para o user adivinhar e responda se acertou ou não
from random import randint
computador = randint(0,5) #print("numero: {}".format(computador)) #escolhe o num aleatorio
print("-=-" * 20)
print("Tente adivinhar o número que eu escolhi entre 0 e 5: ")
print("-=-" * 20)
palpite = int(input("Qual número você acha que é? ")) #jogador tenta adivinhar
if palpite == computador:
    print("Parabéns! Você acertou!")
else:
    print("Game Over. Eu escolhi o número {}".format(computador))