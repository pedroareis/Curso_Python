import random

print('=-=' * 12)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
print('=-=' * 12)

num = int(input('Em que número eu pensei? '))
opções = [0,1,2,3,4,5]
pc = random.choice(opções)
if pc == num:
    print('PARABÉNS, você acertou')
else:
    print('Errou... Eu pensei em {} e você disse {}'.format(pc,num))

