numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] conversão para BINÁRIO
[ 2 ] conversão para OCTAL
[ 3 ] conversão para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Número invalido, digite um número de 1 a 3')



