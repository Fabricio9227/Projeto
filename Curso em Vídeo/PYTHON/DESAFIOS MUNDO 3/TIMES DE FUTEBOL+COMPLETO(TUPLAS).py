from time import sleep
times = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")
print("="*50)
print("{:^50}".format("DADOS DO BRASILEIRÃO 2019"))
print("="*50)
opcao = 0 #OPÇÃO RECEBE O VALOR INICIAL DE ZERO
while opcao != 8: #ENQUANTO OPÇÃO FOR DIFERENTE DE 8, FAÇA
    sleep(3)
    opcao = int(input('''[1] O Campeão do campeonato
[2] Classificados para fase de grupos da Libertadores 
[3] Classificados para Pré - Libertadores 
[4] Classificados para fase de grupos da Copa Sul-Americana
[5] Rebaixados para serie B
[6] Posição e situação de determinado time
[7] Tabela completa
[8] Sair do programa do brasileirão
Digite: ''')) #PEDE PARA DIGITAR UM NUMERO DE 1 Á 8
    print("="*50)
    if opcao == 1: #SE A OPÇÃO FOR 1
        print("O campeão foi o {}".format(times[0])) #MOSTRE O TIME DA POSIÇÃO ZERO
    elif opcao == 2:
        print(f"Classificados para Libertadores 2020: {times[:6]}") #MOSTRE OS 5 PRIMEIROS
    elif opcao == 3:
        print(f"Classificados para Pré - Libertadores 2020: {times[6:8]}") #MOSTRE DA POSIÇÃO 6 ATÉ A POSIÇÃO 7 
    elif opcao == 4:
        print(f"Classificados para Sul-Americana 2020: {times[8:14]}") #MOSTRE DA POSIÇÃO 8 ATÉ A 13
    elif opcao == 5:
        print(f"Rebaixados para Segunda Divisão: {times[-4:]}") #MOSTRE OS 4 ULTIMOS
    elif opcao == 6: #SE A OPÇÃO FOR 6
        time = str(input("Escreva o nome do seu time: ")).strip().title() #TIME RECEBE UM INPUT
        if time in times: #SE TIME ESTIVER EM TIMES
            print(f"O {time} ficou na {times.index(time)+1}º Posição") #O TIME FICOU NA POSIÇÃO INFORMADA ATARVÉS DO INDEX QUE LOCALIZA O TIME POR ESCRITA
            print("Situação: ",end="") #SITUAÇÃO DO TIME
            if times.index(time) == 0: #SE A POSIÇÃO FOR ZERO
                print("Campeão brasileiro e está na Libertadores")
            elif times.index(time) >= 1 and times.index(time) <= 5: #SE A POSIÇÃO ESTIVER ENTRE 1 E 5
                print("Está na Libertadores")
            elif times.index(time) >= 6 and times.index(time) < 8: #SE A POSIÇÃO ESTIVER ENTRE 6 E 8
                print("Está na Pré - Libertadores")
            elif times.index(time) >= 8 and times.index(time) <= 13:
                print("Está na Copa Sul-Americana")
            elif times.index(time) >= 16: #SE O TIME ESTIVER NA POSIÇÃO ACIMA OU IGUAL A 16
                print("Está Rebaixado para a Serie B")
            else:
                print("Ficou na Serie A, porém não se classificou para nenhuma outra competição")
        else:
            print("O {} não participou do Brasileirão 2019".format(time))
    elif opcao == 7: #SE A OPÇÃO FOR 7
        cont = 0 #RECEBE UM CONTADOR PARA DIZER QUANTOS TIMES ESTÃO NA TABELA
        print("="*50)
        print("{:^50}".format("TABELA DO BRASILEIRÃO 2019"))
        print("="*50)
        for tabela in times:
            print(f"{cont + 1}º {tabela}")
            cont += 1
    print("=" * 50)
print("Fim do programa do campeonato brasileiro")