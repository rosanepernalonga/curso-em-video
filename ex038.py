#leia dois numeros, compare qual é o maior, menor ou se são iguais.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo numero: '))
if a > b:
    print('O primeiro número á maior que o segundo.')
elif b > a:
    print('O segundo número é maior que o prmeiro.')
else:
    print('Os números digitados são iguais.')