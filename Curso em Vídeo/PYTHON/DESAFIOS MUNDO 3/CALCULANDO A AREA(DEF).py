def calcular(larg, comp): #Crio a função calcular que recebe como parametro "larg" e "comp" que será as medidas digitadas no programa principal. para isso será necessario cria-las fora da nossa função
    area = larg * comp #Criada a função area que faz o calculo da area
    print(f'A área de um terreno de {larg} x {comp} é {area:.2f}m²') 

#Programa principal

print('Controle de Terrenos')
print('-' * 20) #Divisor 

#Criando as variáveis para podermos usar a nossa função calcular:

larg = float(input('Largura [L]: ')) 
comp = float(input('Comprimento [C]: '))

#Com as variáveis criadas, podemos solicitar a função calcular

calcular(larg, comp)




