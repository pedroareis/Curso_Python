print('JOKENPÔ\n ')
import random
import time

jogo = str(input('Pedra, papel ou tesoura? ')).strip().lower()
lista = ['pedra','papel','tesoura']
pc = random.choice(lista)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(0.5)
print('-='*12)
print('Você jogou {}!\nComputador jogou {}!'.format(jogo, pc))
print('-='*12)

if jogo == 'pedra':
    if pc == 'pedra':
        print('EMPATE')
    elif pc == 'papel':
        print('\033[31mPC GANHOU!')
    elif pc == 'tesoura':
        print('\033[35mVOCÊ GANHOU')
elif jogo == 'papel':
    if pc == 'pedra':
        print('\033[35mVOCÊ GANHOU')
    elif pc == 'papel':
        print('EMPATE')
    elif pc == 'tesoura':
        print('\033[31mPC GANHOU')
elif jogo == 'tesoura':
    if pc == 'pedra':
        print('\033[31mPC GANHOU')
    elif pc == 'papel':
        print('\033[35mVOCÊ GANHOU')
    elif pc == 'tesoura':
        print('EMPATE')





