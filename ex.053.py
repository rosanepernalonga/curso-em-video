#DESCUBRA SE A FRASE DIGITADA É UM PALINDROMO
frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]
if inverso == junto:
    print('{} e {} , portanto temos um palindromo '.format(junto, inverso))
else:
    print('a frase {} não é um palindromo'.format(junto))