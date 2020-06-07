nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é:', nome.upper())
print('Seu nome em minúsculo é:', nome.lower())
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))

