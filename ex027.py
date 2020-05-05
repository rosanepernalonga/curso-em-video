# Faça um programa que leia o nome completo de uma pessoa, mostre em seguida o primeiro e ultimo nome separadamente
fullName = str(input('Digite seu nome completo: ')).strip().title()
splitfullName = fullName.split()
print('Nome: ', splitfullName[0])
print('Sobrenome', splitfullName[-1])
