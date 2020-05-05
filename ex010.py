#crie um programa que leia quanto de dinheiro a pessoa tem na carteira e mostre a conversão em dólares
#considere dolar = 3.27 ... hj 23/01/2020 está 4.17
d = float(input('Quanto você tem na carteira '))
print('Você pode trocar esse valor por US${:.2f} dólares.'.format(d/3.27))