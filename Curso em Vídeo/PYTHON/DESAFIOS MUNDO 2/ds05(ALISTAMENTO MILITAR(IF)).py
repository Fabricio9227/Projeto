from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format((saldo)))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade <= 21:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format((saldo)))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você está já passou da fase de alistamento.')
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))


    #QUOTE IMPORTANTE:
    
    #CRIAMOS VARIÁVEIS DENTRO DE ESTRUTURAS DE CONDIÇÃO, ESSAS VARIÁVEIS SÓ TEM VALOR DENTRO DA CONDIÇÃO QUE ELA ESTÁ IDENTADA. PODE SER USADA EM OUTRA CONDIÇÃO COM O MESMO NOME E VALOR (OU UM VGALOR DIFERENTE PARA AQUELA CONDIÇÃO).
    