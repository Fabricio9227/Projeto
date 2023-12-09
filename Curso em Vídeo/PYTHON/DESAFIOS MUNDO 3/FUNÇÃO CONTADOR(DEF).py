from time import sleep

def contador(i, f, p): #INICIO, FIM E PASSO 

    #Verificando passo 0 e numeros negativos

    if p < 0: #Se passo for menor que 0 (negativo)
        p *= -1 #Passo é convertido para negativo
    if p == 0: #Se passo for igual a 0
        p = 1 #Passo recebe 1
    
    print('-=' * 20)
    print(f'Contagem de {i} até {f}, de {p} em {p}')
    sleep(2.0)

#Verificando inicio e fim:

    if i < f: #Se o inicio for maior que o fim
        cont = i #contador recebe o valor de incio
        while cont <= f: #Enquanto meu contador for menor ou igual ao fim
            print(f'{cont} ', end='', flush=True) #Printa a contagem. Flush permite que possamos ver a contagem acontecendo
            sleep(0.5) #A cada número, durma 0.5 segundos
            cont += p #contador recebe + p
        print('FIM!')
    else: #Se não (se a contagem for do maior pro menor)
        cont = i #contador recebe o valor de inicio
        while cont >= f: #Enquanto contador for maior ou igual a fim
            print(f'{cont} ', end='', flush=True) #Printa a contagem. Flush permite que possamos ver a contagem acontecendo
            sleep(0.5)
            cont -= p #Contagem recebe menos passo, como se fosse passos para tras
        print('FIM!')
        print('-=' * 20)    

#Programa Principal
contador(1, 10, 1) #função contador recebendo respectivasmente os valores(i, f, p)
contador(10, 0, 2)
print('-=' * 20)

print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)



