pares = 0
for c in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares += num
print('A soma dos números pares é {}'.format(pares))
