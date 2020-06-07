n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2)/2

if media < 5.0:
    print('Sua nota final é {:.1f}. \033[31mReprovado!'.format(media))
elif media >= 5.0 and media < 7:
    print('Sua nota final é {:.1f}. \033[33mRecuperação'.format(media))
else:
    print('Sua nota final é {:.1f}. \033[36mAprovado'.format(media))