import os
from tkinter.filedialog import askdirectory

CaminhoDaPasta = askdirectory(title='Selecione uma pasta')
list_arquivos = os.listdir(CaminhoDaPasta)

locais = {
    'Imagens': ['.png', '.JPG', '.jpg'],
    'Músicas': ['.wav', '.mp3'],
    'Pdfs': ['.pdf'],
    'Docs': ['.RFT'],
    'ZIP': ['.zip']
}

for arquivo in list_arquivos: #Criada a variável "arquivo". Para o arquivo dentro de lista, execute:
    
    nome, extensão = os.path.splitext(f'{CaminhoDaPasta}/{arquivo}')#A variável nome e extensão recebem respectivamente, uma troca pelo caminho da pasta com a extensão do arquivo

    for pasta in locais:#Para cada "pasta" na dicionario "locais"

        if extensão in locais[pasta]:#Procure a extensão na lista de "locais"

            if not os.path.exists(f"{CaminhoDaPasta}/{pasta}"):#Se não encontrar, a pasta já criada dentro do caminho da pasta

                os.mkdir(f"{CaminhoDaPasta}/{pasta}")#Crie uma pasta para alocar a extensão.

            os.rename(f"{CaminhoDaPasta}/{arquivo}", f"{CaminhoDaPasta}/{pasta}/{arquivo}")#Dentro da função há respectivamente, o antes e o depois de como o arquivo ficou renomeado. Um pequeno acrescimo com a variavel pasta no novo nome, pois agora ele estará na pasta criada para a extensão do mesmo.
print('Sua pasta está organizada agora!')
