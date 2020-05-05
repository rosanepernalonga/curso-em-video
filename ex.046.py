#contagem regressiva de 10 segundos (pausa de 1 segundo entre)
from time import sleep
for r in range(10, 0, -1):
    print(r)
    sleep(1)
print('Happy new year \o/')