mensagem = input('Digite algo: ')
print('O tipo primitivo dessa mensagem é :', type(mensagem))
print('É um número?', mensagem.isnumeric())
print('É só alfabetico?', mensagem.isalpha())
print('Só tem espaços?', mensagem.isspace())
print('É alfanumérico?', mensagem.isalnum())
print('Tá em capslock?', mensagem.isupper())
print('Tá em minúscula?', mensagem.islower())
print('Está capitalizada?', mensagem.istitle())



