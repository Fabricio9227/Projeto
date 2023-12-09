itens = ('Banana', 1.80,
           'Maça', 2.90,
           'Lápis', 4.99,
           'Caderno', 10.99,
           'Melancia', 8.80,
           'Mochila', 20.99,
           'Caneta', 1.99)

print('-' * 37)
print('LISTAGEM DE PREÇOS'.center(37))
print('-' * 37)

for item in range(0, len(itens)): #Para item no range de 0 até o tamanho da lista
    if item % 2 == 0: #Verificar se o item é par
        print(f'{itens[item]:.<30}', end="") #se for par, ordena ele á esquerda com 30 pontos depois dele
    else: 
        print(f'R${itens[item]:>5.2f}') #Se for impar, alinha na direita com 5 espaços e com a formatação de 2 casas decimais pros


