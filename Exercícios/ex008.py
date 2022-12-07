m = float(input('Quantos metros? '))
cm = m * 100
mm = m * 1000
dc = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('{:.0f} metros dá: \n{:.1f} cm \n{:.1f} mm \n{:.1f} dc \n{:.1f} dam \n{:.1f} hm \n{:.1f} km'.format(m, cm, mm, dc, dam, hm, km))
