print('+=+'*20)
print('Analisador de triângulos')
print('+=+'*20)
r1 = float(input('tamanho reta 1: '))
r2 = float(input('tamanho reta 2: '))
r3 = float(input('tamanho reta 3: '))

if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:
    print('\033[1;31mNÃO\033[m é possível formar um triângulo')
else:
    print('Com os valores de segmento {}, {} e {} é possível formar um triângulo'.format(r1,r2,r3))