class Cliente():

    def __init__(self, nome, email, plano): #Criação da função init (que é a "pai" das outras funções criadas posteriormente)
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']#Crio uma caracteristica fixa e imutável
        if plano in self.lista_planos: #Se o plano estiver na lista de planos
            self.plano = plano #plano é aceito e executado
        else: #Se não
            raise Exception('Plano inválido') #Suba um erro dizendo "Plano inválido"
        

    def MudarDePlano(self, novo_plano): #Crio a função mudardeplano, que recebe variáveis self e novo plano como caracteristicas da função
        if novo_plano in self.lista_planos:#Se o novo plano estiver na lista de planos
            self.plano = novo_plano #Plano recebe um novo valor
            print(f'Seu plano foi alterado com sucesso para {novo_plano}!')
        else: #Se não
            print('Plano inválido')


    def VerFilme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Faça um upgrade de plano para poder assistir')
        else:
            raise Exception('Plano inválido')
        
    
cliente = Cliente('Fabricio', 'fabricio@gmail.com', 'basic') #Crio o meu usuário cliente usando as variáveis criadas na função init
print(cliente.plano) #Mostre o plano da variável cliente


#Botão de upgrade

cliente.MudarDePlano('premium')
print(cliente.plano)