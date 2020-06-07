real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real / 5.80

print('Com R${:.2f}, você pode comprar US${:.2f} dólares'.format(real,dolar))