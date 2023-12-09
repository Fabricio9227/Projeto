numero = (int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')))
print(f'Você digitou os valores {numero}')
print(f'O numero 9 apareceu {numero.count(9)} vezes.') #Função 'count' conta o número ou string passado como parametro dentro das '()'
if 3 in numero: #Se 3 estiver em numero
        print(f'O numero {3} ficou na posição {numero.index(3)+1}º')
print('Os valores pares digitados foram: ', end='')
for n in numero: #Para cada item em numero
        if n % 2 == 0: #Verifica se numero é divisivel por 2:
            print(n, end=" ") #Print todos os elementos divisiveis por 2
        

