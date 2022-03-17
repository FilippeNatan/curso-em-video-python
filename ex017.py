from math import pow, sqrt
catetoOposto = float(input('Informe o valor do cateto oposto:'))
catetoAdjacente = float(input('Informe o valor do cateto adjacente:'))
hipotenusa = (pow(catetoOposto, 2) + (pow(catetoAdjacente, 2)))
'''hipotenusa = math.hypot(catetoOposto, catetoAdjacente)'''
print('O valor da hipotenusa é {:.2f}.'.format(sqrt(hipotenusa)))

