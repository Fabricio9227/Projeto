primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (11 - 1) * razão

for pa in range(primeiro, décimo, razão):
    print('{}'.format(pa), end=' -> ')
print('Acabou!')