times = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")

print('=-' * 20)
print(f'Lista dos times do Brasileirão {times}')
print('=-' * 20)
print(f'Os 5 primeiros times são {times[0:5]}')
print('=-' * 20)
print(f'Os 4 últimos são {times[-4:]}')
print('=-' * 20)
print(f'Em ordem alfabetica {sorted(times)}')
print('=-' * 20)
print(f'O Gremio está na {times.index("Gremio")+1} posição na tabela')