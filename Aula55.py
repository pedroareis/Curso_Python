
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(c)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('maior peso foi lido foi de {:.1f}Kg e o menor {:.1f}Kg'.format(maior,menor))