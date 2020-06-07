num = int(input('Digite o número inicial: '))
raz = int(input('Digite a razão da PA: '))
pa = num + (10-1) * raz
print('Uma PA iniciando em {} com razão {} tem:'.format(num,raz))
for c in range(num, pa+raz , raz):
    print((c), end=' ')
print('\nnos seus 10 primeiros elementos')
