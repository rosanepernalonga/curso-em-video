#leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
#soma dos quadrados dos catetos é igual ao quadrado da hipotenusa
'''import math
co = float(input('digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
hip = math.sqrt(((co ** 2) + (ca ** 2)))
print('O comprimento da hipotenusa é: {:.2f}'.format(hip))'''
#outra forma de resolver sem importar nada:
co = float(input('digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
hip = ((co ** 2) + (ca ** 2)) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hip))