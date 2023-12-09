#APLICANDO O PASS NO IF

for num in range(1, 11): #CRIA UMA LISTA DE 1 ATÉ 10
    if num % 2 == 0: #SE O RESTANTE DE NUM/2 FOR IGUAL A ZERO
        pass #DESCONSIDERE E CONTINUE A LISTA
    else:
        print(num)
print('Laço encerrado')
