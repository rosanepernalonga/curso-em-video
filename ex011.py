#leia a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintar.
#cada litro de tinta pinta 2m²
a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
tinta = (a*l)/2
print('A quantidade de tinta necessária é {:.2f} litro(s)'.format(tinta))