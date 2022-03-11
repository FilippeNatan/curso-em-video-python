largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))
area = largura*altura
print('A área total é {}m² e você precisará de {} litro(s) de tinta para pintar.'
      .format(area, area/2))
