from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
anguloRadiano = radians(angulo)
seno = sin(anguloRadiano)
cosseno = cos(anguloRadiano)
tangente = tan(anguloRadiano)
print('O Seno do angulo é {:.2f}, o Cosseno é {:.2f} e a Tangente é {:.2f}.'.format(seno, cosseno, tangente))
