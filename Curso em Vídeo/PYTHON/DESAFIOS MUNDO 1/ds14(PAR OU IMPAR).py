num = int(input('Digite um número para saber se ele é impar ou par: '))
res = num % 2

if res == 1:
    print('O numero {} é um número ÍMPAR'.format(num))
else:
    print('O numero {} é um número PAR'.format(num))
