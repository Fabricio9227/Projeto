sexo = str(input('Informe seu sexo: [F/M] ')).strip().upper()[0]#Strip elimina os espaços. Upper deixa as letras em caixa alta. e o indice '0' indica que será considerada apenas a primeira letra da palavra
while sexo not in 'MF':#Enquanto sexo não estiver em M e F
    sexo = str(input('Dado inválido. Por favor, digite seu sexo: [F/M] ')).strip().upper()[0]#Sexo recebe o valor para digitar novamente o sexo, este loop será repetido enquanto o usuário digitar um dado inválido
print('Sexo {} registrado com sucesso'.format(sexo))