frase = str(input('Digite uma frase: ')).strip()
lower = frase.lower()
print('A letra A aparece {} vezes na frase'.format(lower.count('a')))
print('A primeira letra A aparece na posição {}'.format(lower.find('a')+1))
print('A última letra A aparece na posição {}'.format(lower.rfind('a')+1))
