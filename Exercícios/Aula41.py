import datetime
ano = int(input('Digite o ano do seu nascimento: '))
hoje = datetime.date.today().year

idade = hoje - ano

if idade <= 9:
    print('Você tem {} anos, sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, sua categoria é JUNIOR'.format(idade))
elif idade <= 20:
    print('Você tem {} anos, sua categoria é SÊNIOR'.format(idade))
else:
    print('Você tem {} anos, sua categoria é MASTER'.format(idade))