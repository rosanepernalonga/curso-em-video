# Faça um programa que leia uma frase pelo teclado (?) e mostre
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela ultima vez
frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra a aparece: {} vezes'.format(frase.count('a')))
print('A letra a aparece pela primeira vez no índice: ', frase.find('a'))
print('A letra a aparece pela última vez no índice: ', frase.rfind('a'))

