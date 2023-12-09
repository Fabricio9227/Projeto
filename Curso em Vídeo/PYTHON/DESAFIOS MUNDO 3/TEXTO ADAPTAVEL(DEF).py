def escreva(msg): #Cria uma função com nome de 'escreva' que recebe 'msg' (mensagem) como parametro, msg será o que será digitado dentro das '( )'
    tam = len(msg) + 4 #Criada a variável tam que irá acompanhar o tamanho da mensagem + 4 "~"
    print('~' * tam) #O número de ~ que terá será de acorde com o tamanho da mensagem
    print(f'  {msg}')
    print('~' * tam)

#Programa Principal
escreva('Olá mundo!')
escreva('Fabricio Martins')