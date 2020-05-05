#calcule a média de duas notas. <5 reprovado, entre 5 e 6.9 recuperação, >7 aprovado.
nota1 = float(input('Nota da primeira atividade: '))
nota2 = float(input('Nota da segunda atividade: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média foi {}. Você foi reprovado.'.format(media))
elif media > 5 and media < 6.9:
    print('Sua média foi {}. Você ficou de recuperação.'.format(media))
elif media > 7:
    print('Sua média foi {}. Você foi aprovado, parabéns!'.format(media))