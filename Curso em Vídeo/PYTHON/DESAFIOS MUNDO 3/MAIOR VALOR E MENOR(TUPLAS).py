from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os numeros sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f'\n O maior valor sorteado foi {min(numeros)}')