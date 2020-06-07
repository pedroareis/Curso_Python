num = int(input('Digite um número para saber se ele é primo: '))
count = 0

for c in range(1, num+1, 1):
    if num % c != 0:
        print('\033[31m{}\033[m'.format(c), end=' ')
    else:
        print('\033[33m{}\033[m'.format(c), end=' ')
        count += 1

if count > 2:
    print('\n{} é divisível por {} números\nentão ele \033[31mNÃO\033[m é primo'.format(num,count))
else:
    print('\n{} só é divisível por 1 e por ele mesmo\nentão ele \033[33mÉ\033[m primo'.format(num))
