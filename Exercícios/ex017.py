'''ca = int(input('Qual o valor do cateto adjacente? '))
co = int(input('Qual o valor do cateto oposto? '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(h))'''

import math
ca = int(input('Qual o valor do cateto adjacente? '))
co = int(input('Qual o valor do cateto oposto? '))
h = math.hypot(ca, co)
print('A hipotenusa vale {:.1f}'.format(h))
