#leia um valor  em metros e o exiba em convertido em centímetros e milímetros
m = float(input('Digite um número em metros '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a: \n {}km \n {:.3f}hm \n {}dam \n {:.0f}cm \n {:.0f}mm'.format(m, km, hm, dam, cm, mm))