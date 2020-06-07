salário = float(input('Calculadora de aumento salarial. Digite um valor: '))
if salário <= 1250.:
    aumento = salário * 1.15
    v = 15
else:
    aumento = salário * 1.1
    v = 10
print('O aumento salarial foi de {}%, passando de R${:.2f} para R${:.2f}'.format(v,salário, aumento))
