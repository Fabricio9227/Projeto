s = 0
for c in range(0, 4):#Cria uma estrutura de repetição que será executada 4 vezes (de 0 até 3)
    n = int(input('Digite um número: '))#Peço para o usuário para inserir um número 4 vezes
    s += n #Uso a variável "s" para somar "n"
print('O somatório de todos os valores foi {}'.format(s))