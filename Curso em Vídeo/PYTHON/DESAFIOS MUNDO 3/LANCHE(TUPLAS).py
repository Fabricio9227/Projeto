# Tuplas são IMUTÁVEIS

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)): #Para cada 'cont' no range de 0 até o tamanho da tupla de lanche
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #Mostre 'cont' de lanche

# for comida in lanche:
#    print(f'Eu vou comer {comida}')

print('Comi pra caramba!')

print(lanche[1:3])
print(lanche[:2])
print(sorted(lanche)) #A funcionalidade sorted organiza os elementos da tupla em ordem