homens = 0
homensid = 0
mulheres = 0
mulheresid = 0
idadetot = 0

for c in range(1,6):
    print('----- {}a PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip().capitalize()
    idadetot += idade
    if sexo == 'M':
        homens += 1
        if c == 1:
            homensid = idade
            homemvelho = nome
        elif idade > homensid:
            homensid = idade
            homemvelho = nome
    elif sexo == 'F':
        mulheres += 1
        if c == 1:
            mulheresid = idade
            mulhervelha = nome
        elif idade > mulheresid:
            mulheresid = idade
            mulhervelha = nome

print('A média de idade do grupo é de {} anos.'.format(idadetot/5))
print('O homem mais velho tem {} anos e se chama {},\ne a mulher mais velha tem {} anos e se chama {}.'.format(homensid, homemvelho, mulheresid, mulhervelha))
print('São {} mulheres e {} homens nesse grupo.'.format(mulheres, homens))