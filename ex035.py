#leia comprimento de 3 retas e diga se elas podem formar um triangulo ou não
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print("Os segmentos informados podem formar um triangulo")
else:
    print("Os segmentos informados NÃO podem formar um triangulo")