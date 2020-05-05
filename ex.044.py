#calcule o preço do produto considerando a forma de pagamento.
#1 a vista dinheiro/cheque: 10% de desconto
#2 a vista no cartao: 5% de desconto
#3 em até 2x sem alteração
#4 acima de 3x + 20% de juros
precoInicial = float(input('Qual o valor inicial do produto desejado? R$ '))
pag = input('Escolha a forma de pagamento: 1) dinheiro/cheque, '
            '2) cartão de crédito (á vista), 3) 2x no cartão sem '
            'juros, 4) a partir de 3x ')
if pag == '1':
    print('Com o pagamento em dinheiro ou cheque você terá 10 % de desconto. O valor será: R$ {}'
          .format(precoInicial - (precoInicial * 10 / 100)))
elif pag == '2':
    print('À vista no cartão você terá 5% de desconto. O valor será: R$ {}'
          .format(precoInicial - (precoInicial * 5 / 100)))
elif pag == '3':
    print('Parcelando até 2x não tem cobrança de juros, nem desconto')
elif pag == '4':
    print('Acima de 3x será cobrado 20% de juros. O valor total será: R$ {}'
          .format(precoInicial + (precoInicial * 20 / 100)))