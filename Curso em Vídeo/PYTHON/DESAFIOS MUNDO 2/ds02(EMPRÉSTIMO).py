casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestação = casa / (anos * 12)# O valor da casa dividido por quantos anos ele quer pagar X 12 meses
minimo = salario * 30 / 100 # O valor do salário X 30 que é o desconto / por 100

print('Para pagar uma casa  de R${:.2f} em {:.2f} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))

if prestação <= minimo: # Se empréstimo for menor ou igual ao valor de 30% do salário (lembrando que não pode ultrapassar 30%)
    print('Empréstimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO.')