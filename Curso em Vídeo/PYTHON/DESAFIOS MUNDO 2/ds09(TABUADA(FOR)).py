num = int(input('Digite um número inteiro: '))

for tabuada in range(0,11):
    res = num * tabuada
    print('{} x {} = {}'.format(num, tabuada, res))
print('FIM!')
