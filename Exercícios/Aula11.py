l = float(input('Qual é a largura da sua parede? '))
h = float(input('Qual é a altura da sua parede? ' ))

a = l*h
tinta = a/2

print('Sua parede tem a dimensão de {}m x {}m e sua área é {}m2.\nPara pintar essa parede, você precisará de {}l de tinta'.format(l,h,a,tinta))
