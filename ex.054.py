#crie um programa que leia o ano de nascimento de 7 pessoas. no final mostre quantas sao maiores de 18 e quantas nao.
maior = 0
menor = 0
for p in range(1, 8):
    ano = int(input('Digite o ano que a pessoa nasceu: '))
    if ano >= 2002:
        menor += 1
    else:
        maior += 1
print('Temos {} pessoa(s) maior(es) de 18 anos e {} pessoa(s) menor(es).'.format(maior, menor))
