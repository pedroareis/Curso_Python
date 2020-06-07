num = int(input('Digite um número para saber sua tabuada: '))
print('A tabuada do {} é:'.format(num))
for c in range(1,11,1):
    print('{} x {:2} = {}'.format(num, c, num*c))

