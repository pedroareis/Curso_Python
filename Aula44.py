produto = float(input('Qual é o valor do produto?\nR$ '))
cond = int(input('(1) À vista\n(2) 2x sem juros\n(3) Até 12x (20%/mês)\n '))

if cond == 1:
    avista = int(input('(1) Dinheiro (10% desc.)\n(2) Cartão (5% desc.)\n '))
    if avista == 1:
        print('À vista em DINHEIRO seu produto de R${:.2f} custará R${:.2f}.'.format(produto, (produto*0.9)))
    elif avista == 2:
        print('À vista no CARTÃO seu produto de R${:.2f} custará R${:.2f}.'.format(produto, (produto*0.95)))
elif cond == 2:
    print('Parcelado em 2x, sua parcela será de R${:.2f} sem juros.'.format(produto/2))
elif cond == 3:
    parcelado = int(input('Em quantas parcelas você quer pagar (3-12)?\n '))
    if parcelado >= 3 and parcelado <= 12:
        print('Parcelado em {}x, seu produto custará R${:.2f}, com parcelas de R${:.2f}.'.format(parcelado,(produto*1.2),((produto*1.2)/parcelado)))
    else:
        print('Selecione uma quantidade parcelas válida (3-12).')
else:
    print('Selecione uma opção válida.')