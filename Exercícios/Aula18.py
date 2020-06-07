import math
angulo = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O ângulo de {:.2f} tem:\nSENO = {:.2f}\nCOSSENO = {:.2f}\nTANGENTE = {:.2f}'.format(angulo,sen,cos,tan))
