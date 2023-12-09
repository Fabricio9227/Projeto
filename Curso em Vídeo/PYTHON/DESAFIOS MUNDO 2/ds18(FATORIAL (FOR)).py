numero = int(input('Digite um número para calcular sua fatorial: '))
cont = numero #Contador recebe o numero inicial digitado pelo usuário
fatorial = 1 #Fatorial recebe o valor nulo inical de 1, por se tratar de uma multiplicação
for numero in range(numero, 0, -1): #é criada uma lista em ordem decrescente do maior numero até o 0
    print('{}'.format(numero), end='')
    print(' X ' if cont > 1 else ' = ', end='') #se meu contador for maior que 1 adiciona 'X', SE NÃO, adiciona um "="    
    fatorial = fatorial * cont #Fatorial passa a valer fatorial X contador
    cont -= 1 #A cada ciclo meu contador passar a valer -1
print('{}'.format(fatorial))
