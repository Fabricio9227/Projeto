from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0 #Opção recebe um valor temporariamente neutro

while opção != 5: #Enquanto a variavel opção for diferente de 5 
    print('-=-' * 12)
    print('Selecione uma das opções a seguir: \n'
      '[ 1 ] Somar \n'
      '[ 2 ] Multiplicar \n'
      '[ 3 ] Maior valor \n'
      '[ 4 ] Novos números \n'
      '[ 5 ] Sair do programa \n')
    opção = int(input(' >>>>>>>>Qual é a sua opção? ')) #Opção recebe o valor que o usuario digita
    sleep(2)
    if opção == 1: #Se a opção for igual a 1
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
        sleep(2)
    elif opção == 2: #Se a opção for igual a 2
        produto = n1 * n2
        print('A multiplicação de {} X {} é {}'.format(n1, n2, produto))
        sleep(2)
    elif opção == 3: #Se a opção for igual a 4 teste
        if n1 > n2: # Se n1 for maior que n2 
            print('O maior valor é {}'.format(n1))
            sleep(2)
        elif n2 > n1:
            print('O maior valor é {}'.format(n2))
            sleep(2)
        else:
            print('Os valores são iguais')
            sleep(2)
    else:
        n1 = int(input('Digite outro primeiro valor: '))
        n2 = int(input('Digite outro segundo valor: '))

print('Fim do programa! Volte sempre!')
