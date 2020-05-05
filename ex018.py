#leia um angulo qualquer e mostre seno, coseno e tangente
import math
an = float(input('Digite um angulo qualquer: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O seno vale: {:.2f}, o cosseno vale: {:.2f} e a tangente vale: {:.2f}'.format(sen, cos, tan))