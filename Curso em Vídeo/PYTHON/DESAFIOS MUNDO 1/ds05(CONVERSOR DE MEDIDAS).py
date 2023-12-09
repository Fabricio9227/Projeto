medida = float(input('Digite uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dc = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}km, {:.0f}hm, {:.0f}dc, {:.0f}dm, {:.0f}cm e {:.0f}mm'.format(medida, km, hm, dc, dm, cm, mm))