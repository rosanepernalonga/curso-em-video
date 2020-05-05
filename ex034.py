#escreva um programa que pergunte o salário e calcule o valor de seu aumento
#acima de 1250,00 aumento de 10%. inferiores aumento de 15%
salario = float(input("Informe o salário atual: "))
if salario <= 1250:
    salario_novo = salario + (salario * 15 / 100)
else:
    salario_novo = salario + (salario * 10 / 100)
print("Quem ganha R${:.2f} ganhará R${:.2f} a partir de hoje".format(salario, salario_novo))