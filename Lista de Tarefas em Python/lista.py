from time import sleep
#from tkinter import *
#from tkinter import ttk

lista = []
opção = 0
print('-'*37)
print('MENU DE AFAZERES'.center(37))
print('-'*37)

while opção != 5: #Enquanto a opção não for 5
    opção = int(input('''[ 1 ] Adicionar tarefas
[ 2 ] Listar tarefas
[ 3 ] Marcar tarefa como concluída
[ 4 ] Excluir Tarefa
[ 5 ] Sair
Digite: '''))
    sleep(0.5)

    if opção == 1:
        nova_tarefa = input('Adicione uma tarefa à lista: ') #Solicita uma nova tarefa

        tarefa = {'descricao': nova_tarefa, 'status': 'não concluída'} #Armazena a tarefa com Descrição e Status (padrão não concluído)

        lista.append(tarefa) #Adiciona a tarefa nova na lista
        sleep(0.5)

    elif opção == 2:
        print('-'*37)
        for indice, tarefa in enumerate(lista): #Cria uma lista usando variáveis LOCAIS "Indice" e "Tarefa" e enumera a variável global 'lista'

            print(f'{indice + 1}. DESCRIÇÃO: {tarefa["descricao"]}, STATUS: {tarefa["status"]}') #Imprime o indice + 1 para identificar. Descreve a tarefa. Mostra o status atual dela

        print('-'*37)
        sleep(0.5)

    elif opção == 3:
       for indice, tarefa in enumerate(lista):
            
            print(f'{indice + 1}. Descrição: {tarefa["descricao"]}, Status: {tarefa["status"]}') #Imprime com um número de identificação (usando a sua posiçao na lista). A descrição e o status.
            sleep(1)
       numero_tarefa = int(input('Digite o número da tarefa que deseja marcar como concluída: ')) #Numero da tarefa que eu quero concluir

       if 1 <= numero_tarefa <= len(lista): #Se o numero digitado for entre 1 e o numero total de tarefas da lista
            tarefa = lista[numero_tarefa - 1] #Tarefa selecionada é removida da lista

            tarefa['status'] = 'concluída' #Tarefa é concluída

            print('-'*38)
            print(f'Tarefa "{tarefa["descricao"]}" marcada como concluída.') #Imprime a tarefa que foi concluída
            print('-'*38)
    elif opção == 4:
         for indice, tarefa in enumerate(lista):
              
              print(f'{indice + 1}. Descrição: {tarefa["descricao"]}, Status: {tarefa["status"]}')

         excluir = int(input('Qual tarefa você gostaria de excluir: '))

         if 1 <= excluir <= len(lista):
                   tarefa = lista[excluir - 1]
                   print('-'*30)
                   print(f'A tarefa "{tarefa["descricao"]}" foi excluida.')
                   print('-'*30)               
    else:
        print('Você digitou 5.')
print('Saindo do programa. Até mais!')
     
