larg = float(input('Digite a largura aqui: '))
alt = float(input('Digite a altura aqui: '))
area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(larg, alt, area))

print('Você usará {:.1f}L de tinta para pintar a parede'.format(tinta))
