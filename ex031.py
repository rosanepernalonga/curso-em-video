#crie um programa que pergunte a distancia de uma viagem em km e calcule o preço da passagem
#R$0.50 por km para viagens até 200km e R$0.45 para viagens mais longas
distancia = float(input("Qual a distância da viagem? "))
if distancia <= 200:
    passagem = distancia * 0.50
    print("O preço da passagem será: R${:.2f}".format(passagem))
else:
    passagem = distancia * 0.45
    print("O preço da passagem será: R${:.2f}".format(passagem))