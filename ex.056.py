#leia nome, idade e sexo de 4 pessoas. mostre media de idade, nome do homem mais velho e quantas mulheres tem menos de 20
soma_idade = 0
media_idade = 0
homem_maior_idade = 0
homem_mais_velho = ''
quantas_mulheres = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if p == 1 and sexo == 'M':
        homem_maior_idade = idade
        homem_mais_velho = nome
    if sexo == 'M' and idade > homem_maior_idade:
        homem_maior_idade = idade
        homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        quantas_mulheres += 1

media_idade = soma_idade/4
print('A média da idade do grupo é {}. O homem mais velho se chama {} e ele tem {} anos. Neste grupo {} mulheres são menores de 21 anos'.format(media_idade, homem_mais_velho, homem_maior_idade, quantas_mulheres))