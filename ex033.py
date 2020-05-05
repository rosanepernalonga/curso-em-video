# leia 3 numeros e mostra qual é o maior e qual é o menor
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print("O Menor valor é: {} ".format(menor))
maior = c
if b > c and b > a:
    maior = b
if a > c and a > b:
    maior = a
print("O Maior valor é: {}".format(maior))
