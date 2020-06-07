from datetime import date
ano = int(input('Digite um ano que você quer analisar: (digite 0 se quer analisar o ano em que estamos) '))
bi = range(0,10000,4)
if ano == 0:
    ano = date.today().year
if ano in bi and ano % 100 != 0 or ano % 400 == 0:
    print('{} é BISSEXTO'.format(ano))
else:
    print('{} não é BISSEXTO'.format(ano))
