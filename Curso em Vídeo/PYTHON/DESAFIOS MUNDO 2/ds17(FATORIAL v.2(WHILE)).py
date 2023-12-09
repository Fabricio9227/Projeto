numero = int(input('Digite um número para calcular sua fatorial: '))
cont = numero #O contador começa tendo o valor do numero que o usuario digita
fatorial = 1 #fatorial recebe o valor inicial de 1, pois se trata de uma multiplicação e não pode ter o valor de zero
print('Calculando {}! = '.format(numero), end='') #End para não pular a linha
while cont > 0: #Enquanto o contador for maior que 0
    print('{}'.format(cont), end='') #Faça um print do contador no indice atual dele
    print(' x ' if cont > 1 else ' = ', end='') #Faça um print também de um "X" se o contador for maior que 1, se ele for igual a 1 coloque um "="
    fatorial *= cont #Meu fatorial = fatorial X contador.
    cont -= 1 #Meu contador perde um a cada inicio de ciclo
print('{}'.format(fatorial)) #Quando cont for 0, printe essa mensagem