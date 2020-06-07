from math import hypot
ca = float(input('Informe o cateto adjacente: '))
co = float(input('Informe o cateto oposto: '))
hi = hypot(ca, co)

print('A hipotenusa é: {:.2f}'.format(hi))