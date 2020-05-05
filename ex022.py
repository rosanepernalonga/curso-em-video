# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras sem considerar espaços
# Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Maiúsculas: ', nome.upper())
print('Minúsculas: ', nome.lower())
print('Quantidade: ', len(nome)-nome.count(' '))
splitNome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(splitNome[0])))
