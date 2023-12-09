cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: #Loop infinito
    num = int(input('Digite um número de 0 e 20: '))
    if 0 <= num <= 20: #Se 'num' estiver entre 0 e 20
        print(f'Você digitou o número {cont[num]}')
    else: #Se não estiver entre 0 e 20
        print('Tente novamente. ', end='')

    pergunta = input('Gostaria de contiunuar? [s/n] ').lower().strip()[0] #Pergunta se gostaria de continuar. Strip() remove espaços e [0] lê somente a primeira string.
    if pergunta == 'n': #Se a resposta do input for 'n'
        print('Fim')
        break #Encerre o programa
    else: #Se não
        continue #Continue no loop
