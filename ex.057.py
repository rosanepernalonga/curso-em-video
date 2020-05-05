#leia o sexo de uma pessoa, aceite se for m ou f. se estiver errado solicite até digitar certo.
sexo = input('Digite o sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Resposta inválida. Digite novamente: ').upper()
    if sexo == 'M' or sexo == 'F':
        print('Agora está certo. Obrigada!')
print('Obrigada!')