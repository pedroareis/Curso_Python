import datetime
ano = int(input('Digite o ano do seu nascimento: '))
hoje = datetime.date.today().year

idade = hoje - ano
falta = 18 - idade
passou = idade - 18

if idade < 17:
    print('Faltam {} anos para você se alistar'.format(falta))
elif idade == 17:
    print('Ano que vem você deve se alistar')
elif idade == 18:
    print('Esse ano você deve se alistar')
elif idade > 18:
    print('Você deveria ter se alistado há {} anos'.format(passou))