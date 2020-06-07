preço = float(input('Qual é o preço do produto? R$'))
desc = preço * 0.4
print('O produto que custava R${:.2f}, na promoção com desconto de 60% vai custar R${:.2f}.'.format(preço,desc))
