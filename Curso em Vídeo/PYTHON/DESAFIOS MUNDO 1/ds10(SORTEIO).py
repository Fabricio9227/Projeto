import random 
aluno1 = str(input('Qual o nome do aluno? '))
aluno2 = str(input('Qual o nome do aluno? '))
aluno3 = str(input('Qual o nome do aluno? '))
aluno4 = str(input('Qual o nome do aluno? '))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista) #CHOICE irá escolher algum item da lista

print('O aluno escolhido foi {}'.format(escolhido))