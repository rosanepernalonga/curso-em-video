#Aprovação de empréstimo bancario. Perguntar o valor da casa, a renda do comprador e quantos anos será pago.
#o valor da prestação nao pode exceder 30% da renda. o empréstimo será negado.
valor = float(input("Qual o valor do imóvel? "))
renda = float(input("Qual sua renda mensal? "))
tempo = int(input("Quantos anos? "))
parcela = valor / (tempo * 12)
regra = renda * (30 /100)
if parcela < regra:
    print("Seu financiamento foi aprovado e o valor da parcela será: {:.2f}.".format(parcela))
else:
    print("Seu crédito não foi aprovado!")
#fiz sozinha sem ver a resolução antes :P Hooray!