import time#Importa o framework time
for t in range(10, 0, -1):#Quando queremos fazer em ordem decrescente, colocamos na eange do maior pro menor e no final colocamos -1
  print(t)
  time.sleep(1)#A cada número, ele dorme por 1 segundo
print('Acabou o tempo.')
