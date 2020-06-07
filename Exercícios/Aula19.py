import random
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
lista = [a1, a2, a3, a4]

print('Os alunos que vieram hoje foram {}, {}, {} e {}'.format(a1, a2, a3, a4))

sorteado = random.choice(lista)
print('Hoje quem apaga o quadro é: {}!!!'.format(sorteado))


