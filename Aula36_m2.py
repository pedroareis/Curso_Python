casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
t = float(input('Por quantos anos você gostaria de financiar? '))

mes = t * 12
pres = casa / mes
prop = (pres*100)/(salario*0.7)

if (salario * 0.7) > pres:
    print('Crédito aprovado, sua prestação será de R${:.2f}, ela representa {:.1f}% do seu salário'.format(pres,prop))
else:
    print('Crédito negado, a prestação será de R${:.2f} e excede a possibilidade de empréstimo em {:.1f}%'.format(pres,prop))

