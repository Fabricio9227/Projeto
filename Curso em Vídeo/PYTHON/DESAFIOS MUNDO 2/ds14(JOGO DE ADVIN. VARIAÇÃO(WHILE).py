from random import randint#Importa da bibliteca random a função randint (Numero inteiro aleatorio)

computador = randint(0,10) #Computador recebe e escolhe um numero inteiro aleatorio de 0 até 10
print('Olá, sou o seu computador.. Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False #A variavel recebe o valor booleano False
palpites = 0 #Palpites será nosso contador

while not acertou: #Enquanto não acertar
    jogador = int(input('Qual seu palpite? ')) #Jogador digita seu palpite
    palpites += 1 
    
    if jogador == computador: #Se a resposta de jogador for igual ao de computador
        acertou = True #Acertou passa a valer True e encerra o loop
    else: #Se não
        if jogador < computador: #Se o numero de jogador for menor que o de computador
            print('Mais.. Tente mais uma vez: ')
        else: #Se o numero de jogador for maior que o de computador
            print('Menos.. Tente mais uma vez: ')

print('Acertou com {} tentativas. Parabéns!'.format(palpites))
