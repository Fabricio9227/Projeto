from time import sleep

def maior(* num): #função maior recebe como parametro * num que significa que pode receber infinitos numeros
    cont = maior = 0 #Contador e maior recebem e começam o programa com 0
    print('-=' * 20)
    print('Analisando valores passados.. ')
    for valor in num: #Para cada "valor" de "num"
        print(f'{valor} ', end='', flush=True) #Printa numero por numero
        sleep(0.3)
        if cont == 0: #Se contador for igual a 0
            maior = valor #O maior é unico valor digitado
        else: #Se não
            if valor > maior: #Se "valor" for maior que "maior"
                maior = valor #"Maior" recebe o "valor"
        cont += 1 #Contador soma mais um numero
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    

#Programa principal
maior(1, 2, 3, 4)
maior(9, 6, 10, 20)
maior(3, 6)
maior(2)
maior()