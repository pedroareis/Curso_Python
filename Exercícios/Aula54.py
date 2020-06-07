import datetime
hoje = datetime.date.today().year

maior = 0
menor = 0
for c in range(1,8):
    id = int(input('Em que ano você nasceu? '))
    if hoje - id >= 21:
        maior += 1
    elif hoje - id < 21:
        menor += 1
print('{} são maiores de idade e {} são menores'.format(maior,menor))

