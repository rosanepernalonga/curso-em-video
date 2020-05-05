#leia o salário e aplique 15% de aumento
sal = float(input('Salário atual: R$'))
novoSal = sal + (sal*15/100)
print('O Salário R${:.2f} com aumento de 15% é: R${:.2f}'.format(sal, novoSal))