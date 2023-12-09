import json
from cryptography.fernet import Fernet #Importamos a função Fernet do pacote cryptography

def Verificar_Chave(chave_inserida, chave_correta):
        try:
            fernet = Fernet(chave_inserida) #Tenta descriptografar algo usando a chave inserida

            fernet.decrypt(b"") #Se estiver certo, a chave está correta

            return True
        except:
            return False
        

#Função para o usuário inserir a senha de criptografia, que verifica se o usuário tem ou não acesso ás senhas 

def LoginUsuário():
        chave_correta = chave #Chave_correta recebe o valor da chave_lida
        chave_inserida = input('Insira a chave de criptografia: ') #Chave_inserida recebe um input para o usuário digitar a sua senha

        if Verificar_Chave(chave_inserida.encode(), chave_correta):
                print('Acesso PERMITIDO. Agora você pode ver suas senhas.')
                ListarSenhas()
        else:
              print('Acesso NEGADO. Digite novamente sua senha.')


#Função para ser listada as senhas

def ListarSenhas():
    
    with open("senhas.json", "r") as file: #O arquivo em json será aberto como a variavel "file"

        senhas = json.load(file) #Senhas recebe o arquivo em Json que será carregado

        for indice, senha in enumerate(senhas): #Criado um for que contém indice senha com as senhas enumeradas
            
            print(f"{indice + 1}. {senha['descricao']}: {senha['senha']}") #Senha recebe um número de identificação usando indice



#CADA VEZ QUE O CÓDIGO FOR RODADO, SERÁ GERADO UMA NOVA CHAVE



chave = Fernet.generate_key() #Gera uma chave randômica (aleatória) na base 64 



#Criando um arquivo para guardar a chave em formato de texto

arquivo = open('chave.key', 'wb')
arquivo.write(chave)
arquivo.close()

print('-'*len(chave))
print('A CHAVE ABERTA É: '.center(len(chave)))
print(chave)
print('-'*len(chave))



#Acessando e lendo o arquivo da chave.key

arquivo = open('chave.key', 'rb')
chave_lida = arquivo.read()
arquivo.close()

chave_lida = '*'*len(chave_lida)



#Programa Principal

print('-'*len(chave_lida))
print('A CHAVE LIDA É: '.center(len(chave_lida)))
print(chave_lida)
print('-'*len(chave_lida))



LoginUsuário()
