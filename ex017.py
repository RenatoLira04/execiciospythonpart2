import math
co = float(input('Comptimento do cateto oposto:'))
ca = float(input('Comptimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
