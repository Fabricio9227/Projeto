cont = 0
soma = 0
maioridadehomem = 0 
nomevelho = ''
mulhermenos20 = 0

for p in range(0,5):
    print('----- {}° PESSOA'.format(p))
    nome = str(input('Nome: ')).strip
    idade = int(input('idade: '))
    sexo = str(input('Sexo[F/M]: ')).strip
    soma += idade
    cont += 1
    
    if p == 1 and sexo == 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: 
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        mulhermenos20 += 1
    
media =  soma / cont
print('A média de idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo temos um total de {} mulheres com menos de 20 anos'.format(mulhermenos20))