import os

mensagens = [] #Mensagens recebe uma lista vazia

nome = input('Nome: ')

while True:

    os.system('cls') #Sempre que o while se repetir o chat será limpo

    if len(mensagens) > 0: #Se o tamanho da mensagem é maior que zero
        for m in mensagens: #Verifica se tem mensagem já gravadas na lista "mensagens"
            print(m['nome'], "-", m['texto']) #Se tiver ele exibe

    print('___________') #Anderlines separando a lista de mensagens com o chat do usuário

    #Obtendo o texto

    texto = input('mensagem: ') #Campo onde o usuário vai colocar a mensagem
    if texto == 'fim': #Se o texto inserido for "fim"
         break #Quebre a laço de repetição
    
    #Adicionando mensagens na lista "mensagens"

    mensagens.append({ #Append adiciona em mensagens "nome" e "texto" digitado pelo usuário
        "nome": nome,
        "texto": texto
    })