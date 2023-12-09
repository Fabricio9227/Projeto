cont = 0 #Este é o 'CONTADOR'
soma = 0 #Este é o 'ACUMULADOR'
for p in range(1, 501, 2): #Cria uma lista de 1 até 500 pulando de 2 em 2
    if p % 3 == 0: #Faz uma verificação para ver se o número é ímpar
        cont += 1 #Se o número for ímpar, ele irá acrescenta-lo ao nosso contador
        soma += p #E também, irá somar o mesmo    
print('A soma de todos os {} números foi {}'.format(cont, soma))
print('Sua contagem terminou!')