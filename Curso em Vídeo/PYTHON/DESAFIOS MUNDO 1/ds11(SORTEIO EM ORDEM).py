from random import shuffle 
aluno1 = str(input('Qual o nome do aluno? '))
aluno2 = str(input('Qual o nome do aluno? '))
aluno3 = str(input('Qual o nome do aluno? '))
aluno4 = str(input('Qual o nome do aluno? '))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = shuffle(lista) #SHUFFLE irá embaralhar a lista

print('-' * 12)
print('A ordem de apresentação será {}'.format(lista))
print('-' * 12)
