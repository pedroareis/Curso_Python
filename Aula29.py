velocidade = float(input('A que velocidade você está viajando? '))

if velocidade > 80:
    print('Você está {:.0f}km/h acima do limite de velocidade. Sua multa é de R${:.2f}'.format((velocidade - 80), ((velocidade - 80)*7)))
else:
    print('Ótimo, tenha uma boa viagem!')
