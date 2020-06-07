m = float(input('Conversor de medidas.\nQuantos metros? '))
print('{}m é igual a {}km\n{}m é igual a {}hm\n{}m é igual a {}dam\n{}m é igual a {:.0f}dm\n{}m é igual a {:.0f}cm\n{}m é igual a {:.0f}mm'.format(m,(m/1000),m,(m/100),m,(m/10),m,(m*10),m,(m*100),m,(m*1000)))
