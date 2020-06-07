nome = str(input('Digite seu nome: ')).strip()
separado = nome.split()
print('Muito bem vindo!')
print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu último nome é {}'.format(separado[-1]))

