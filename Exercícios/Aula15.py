dias = int(input('Por quantos dias você alugou o carro? '))
rodagem = float(input('Quantos km você rodou? '))

carro = 60
km = 0.15
total = (dias * carro) + (rodagem * km)

print('O aluguel por {} dias, somado com {}km rodados, custou: R${:.2f}.'.format(dias,rodagem,total))
