#leia a idade de um atleta e mostre a categoria.
# <9: mirim, 9 a 14: infantil, 14 a 19: junior, até 20 senior, acima: master
idade = int(input('Qual sua idade? '))
if idade < 9:
    print('A categoria correspondente a sua idade é Mirim')
elif idade >= 9 and idade < 14:
    print('A categoria correspondente a sua idade é Infantil')
elif idade >= 14 and idade < 19:
    print('A categoria correspondente a sua idade é Júnior')
elif idade > 20:
    print('A categoria correspondente a sua idade é Sênior')
elif idade >= 20:
    print('A categoria correspondente a sua idade é Master')