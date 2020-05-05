#escreva um programa que leia a velocidade de um carro.
#se ultrapassar 80km/h mostre uma mensagem dizendo que foi multado
#a multa custa R$7,00 por cada km acima do limite
velocidade = float(input("Qual a velocidade atual do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado por estar acima da velocidade permitida. Valor da multa: R${}".format(multa))
else:
    print("Tenha um bom dia!")