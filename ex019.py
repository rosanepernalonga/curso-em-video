#sortear um dos quatro alunos
import random
aluno1 = input('Digite o nome do aluno1: ')
aluno2 = input('Digite o nome do aluno2: ')
aluno3 = input('Digite o nome do aluno3: ')
aluno4 = input('Digite o nome do aluno4: ')
sorteado = [aluno1, aluno2, aluno3, aluno4]
print('O sorteado é: {}'.format(random.choice(sorteado)))