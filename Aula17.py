from numpy import sqrt
ca = float(input('Informe o cateto adjacente: '))
co = float(input('Informe o cateto oposto: '))
h = sqrt((ca**2)+(co**2))

print('A hipotenusa é: {:.2f}'.format(h))