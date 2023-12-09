soma = 0 #Acumulador
cont = 0 #Contador
for t in range(0, 7):
    num = int(input('Digite um número inteiro: '))
    if t % 2 == 0:
        soma += t
        cont += 1
print('Os números somados foram {} e sua soma foi {}'.format(cont, soma))
print('FIM!')
