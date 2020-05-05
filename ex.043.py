#leia peso e altura e calcule o IMC.
# abaixo de 18.5: abaixo do peso, entre 18 e 25: peso ideal
# 25 a 30: sobrepeso, 30 a 40: obesidade, acima de 40: obesidade mórbida
#altura * altura / peso
altura = float(input('Informe a sua altura (m): '))
peso = float(input('Informe seu peso (Kg): '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Seu peso é considerado abaixo do peso ideal')
elif imc > 18 and imc < 25:
    print('Seu peso é considerado o peso ideal')
elif imc > 25 and imc < 30:
    print('Seu peso é considerado  sobrepeso')
elif imc > 30 and imc < 40:
    print('Seu peso é considerado obesidade')
else:
    print('Seu peso é considerado obesidade mórbida')