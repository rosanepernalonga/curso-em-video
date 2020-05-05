#refaça o ex.35. e mostre que tipo de triangulo será formado.
# equilátero: todos os lados iguais, isósceles: dois lados iguais, escaleno: todos os lados diferentes.
a = int(input('Qual a medida da primeira reta? '))
b = int(input('Qual a medida da segunda reta? '))
c = int(input('Qual a medida da terceira reta? '))
#if a + b > c or b + c > a or c + a > b:
#   print('As medidas informadas formam um triangulo!')
if a + b > c or b + c > a or c + a > b:
    print('Essas medidas podem formar um triangulo', end = ' ')
    if a == b and a == c:
        print("equilátero.")
    elif (a != b and a != c and b != c):
        print('escaleno')
    else:
        print('isósceles')
else:
    print('As medidas informadas não podem formar um triângulo.')