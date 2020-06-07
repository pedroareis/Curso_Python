num = int(input('Digite um número inteiro: '))
convert = int(input('Qual é a base de conversão? (1)Binário, (2)Octal, (3)Hexadecimal: '))

if convert == 1:
    print('{} em decimal equivale a {} em binário'.format(num, bin(num)))
elif convert == 2:
    print('{} em decimal equivale a {} em octal'.format(num, oct(num)))
elif convert == 3:
    print('{} em decimal equivale a {} em hexadecimal'.format(num, hex(num)))
else:
    print('Opção inválida, digite um número entre 1 e 3')
