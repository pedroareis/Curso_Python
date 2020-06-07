salário = float(input('Qual é o salário do funcionário? R$'))
aumento = salário + (salário * .15)

print('Um funcionário que ganhava R${:.2f}, com o aumento de 15%, passa a receber R${:.2f}.'.format(salário,aumento))
