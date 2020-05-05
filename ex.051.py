#leia o primeiro termo e a razão de uma pa. no final mostre os 10 primeiros termos dessa progressao
print(30*'=')
print('     10 TERMOS DE UMA PA')
print(30*'=')
primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiroTermo + (10) * razao
for c in range(primeiroTermo, decimo, razao):
    print(c, end=' ')
print('ACABOU')
