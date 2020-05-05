#leia o ano de nascimento. informe se ainda vai se alistar, se é a hora de se alistar ou se já passou.
#Mostre o tempo que falta ou passou
ano = int(input('Qual o ano de nascimento? '))
idade = 2020 - ano
alistamento = 18
if idade == alistamento:
    print('Você já pode se alistar!')
elif idade > alistamento:
    print('Você já poderia ter se alistado há {} anos.'.format(idade-alistamento))
else:
    print('Você poderá se alistar em {} anos.'.format(alistamento-idade))
