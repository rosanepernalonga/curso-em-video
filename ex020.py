#sortear a ordem de apresentação dos trabalhos dos quatro alunos. leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = input('Digite o nome do aluno1: ')
aluno2 = input('Digite o nome do aluno2: ')
aluno3 = input('Digite o nome do aluno3: ')
aluno4 = input('Digite o nome do aluno4: ')
sorteado = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sorteado)
print('A ordem de apresentação será: ')
print(sorteado)