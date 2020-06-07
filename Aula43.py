print('+=+'*20)
print('Calculadora de IMC')
print('+=+'*20)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura**2)

if IMC < 18.5:
    print('Seu IMC é {:.1f}, você está ABAIXO DO PESO'.format(IMC))
elif IMC < 25:
    print('Seu IMC é {:.1f}, você está no PESO IDEAL'.format(IMC))
elif IMC < 30:
    print('Seu IMC é {:.1f}, você está com SOBREPESO'.format(IMC))
elif IMC < 35:
    print('Seu IMC é {:.1f}, você está com OBESIDADE GRAU I'.format(IMC))
elif IMC < 40:
    print('Seu IMC é {:.1f}, você está com OBESIDADE GRAU II (severa)'.format(IMC))
else:
    print('Seu IMC é {:.1f}, você está com OBESIDADE GRAU III (mórbida)'.format(IMC))