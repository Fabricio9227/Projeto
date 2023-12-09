from random import randint

numero = randint(0,5)
print('-=-' * 20)
print('Tente adivinhar o número que estou pensando.. ')
print('-=-' * 20)

usuario = int(input('Digite um número de 0 até 5: '))

if usuario == numero:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você perdeu!')
    print('O número era {} e não {}'.format(numero, usuario))