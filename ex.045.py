#jokenpô = pedra papel e tesoura
from random import randint
jogo = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)

jogador = int(input('''Vamos jogar joquenpô? Esolha uma opção: 
[0] pedra 
[1] papel 
[2] tesoura
Qual sua jogada? '''))
print('-=-' * 10)
print('Eu escolhi {}'.format(jogo[pc]))
print('Você escolheu {}'.format(jogo[jogador]))
print('-=-' * 10)
if pc == 0: #pc jogou pedra
    if jogador == 0:  # jogador jogou pedra
        print('EMPATE')
    elif jogador == 1:  # jogador jogou papel
        print('Você ganhou!')
    elif jogador == 2:  # jogador jogou tesoura
        print('Eu ganhei!')
elif pc == 1: #pc jogou papel
    if jogador == 0:  # jogador jogou pedra
        print('Eu ganhei!')
    elif jogador == 1:  # jogador jogou papel
        print('EMPATE')
    elif jogador == 2:  # jogador jogou tesoura
        print('Você ganhou')
elif pc == 2: #pc jogou tesoura
    if jogador == 0:  # jogador jogou pedra
        print('Você ganhou!!')
    elif jogador == 1:  # jogador jogou papel
        print('Eu ganhei')
    elif jogador == 2:  # jogador jogou tesoura
        print('EMPATE')