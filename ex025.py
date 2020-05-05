# Crie um programa que leia o nome completo de uma pessoa e diga se ela tem o sobrenome 'SILVA'
nomeCompleto = str(input('Digite seu nome completo: ')).strip().title()
print('Silva'in nomeCompleto)