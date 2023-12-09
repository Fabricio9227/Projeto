n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('a soma é {}, a multiplicação fica {}, a divisão fica {}'.format(s,m,d), end=' ')#end significa que a linha não será quebrada
print('a divisão inteira fica {},\n a exponenciação fica {}'.format(di,e))#"\n" significa que a linha vai ser quebrada para uma nova linha