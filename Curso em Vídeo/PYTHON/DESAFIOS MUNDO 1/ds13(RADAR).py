vel = int(input('Qual sua velocidade? '))
multa = (vel-80) * 7


print('Sua velocidade foi de {}km/h'.format(vel))
if vel <= 80:
    print('Você está dentro do limite da via! Dirija com segurança.')
else:
    print('Você foi multado! Dirija com segurança.')
    print('Sua multa é de R${:.2f} reais'.format(multa))