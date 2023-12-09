
lista_de_senhas = [] #Lista de senhas recebe um valor vazio, pois ainda não foi armazenado nada nela

chave = input('Digite a base da sua senha: ')

senha = '' #Senha começa recebendo um valor inicial vazio, pois não foi atribuído nada ainda á ela

for letra in chave:
    if letra in 'Aa':
        senha = senha + '1'
    elif letra in 'Bb':
        senha = senha + '@'
    elif letra in 'Cc':
        senha = senha + '2'
    elif letra in 'Dd':
        senha = senha + '3'
    elif letra in 'Ee':
        senha = senha + '4'
    elif letra in 'Ff':
        senha = senha + '5'
    elif letra in 'Ss': 
        senha = senha + '6'
    elif letra in 'Nn':
        senha = senha + '&'
    else:
        senha = senha + letra
print(f'Uma sugestão de senha segura é: {senha}')