#calcule o preço a pagar sendo que o custo por dia é R$60 + R$0.15 por km rodado.
aluguel = int(input('Quantidade de dias: '))
distancia = float(input('Quantos km rodados: '))
preço = (aluguel * 60) + (distancia * 0.15)
print('O preço da locação é R${:.2f}'.format(preço))
