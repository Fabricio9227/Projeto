num = float(input('Digite seu dinheiro aqui para converter: R$'))
dolar = num / 5.19 
euro = num / 5.50
peso = num / 0.01483
print('Você tem um total de US${:.2f} em dólar e €{:.2f} em euro e ${:.0f} em peso Argentino'.format(dolar, euro, peso))