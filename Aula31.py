km = float(input('Qual a distância da sua viagem em km? '))
if km > 200.:
    print('Sua passagem custará R${:.2f}'.format(km * 0.45))
else:
    print('Sua passagem custará R${:.2f}'.format(km * 0.50))