#ESTRUTURA DE REPETIÇÃO "FOR"


#SUA SINTAXE É: "for" <variável> "in" <sequência>


nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)

#ESTRUTURA DE REPETIÇÃO WHILE

#SUA SINTAXE É: "while" <variável>: <instruções>

palavra = input('Entre com uma palavra: \n ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')

#WHILE INFINITO

#SUA SINTAXE É: "while True:"

while True:
    palavra = input('Entre com uma palavra: \n')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço')

#APLICANDO O BREAK EM VARIAS ESTRUTURAS DE REPETIÇÃO

while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
                break  # este break é do segundo laço
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')

