from math import factorial #Importamos a função de fatorial do framework math
n = int(input('Digite um número para calcular sua fatorial: ')) #Pedimos ao usuário para digitar um numero
f = factorial(n) #F recebe a função fatorial de n (numero que o usuario digitou)
print('a fatorial de {}! é {}'.format(n,f))