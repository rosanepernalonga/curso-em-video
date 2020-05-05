#leia o preço e aplique 5% de desconto
preco = float(input('Preço atual: R$'))
print('O preço com desconto de 5% é: R${:.2f}'.format(preco-((preco*5)/100)))