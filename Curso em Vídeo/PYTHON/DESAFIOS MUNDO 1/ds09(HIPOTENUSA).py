import math

CaO = float(input('Digite aqui o valor do seu cateto oposto: '))
CaA = float(input('Digite aqui o valor de seu cacteo adjacente: '))
hip = math.hypot(CaA, CaO)

print('Sua hipotenusa vale {:.2f}'.format(hip))