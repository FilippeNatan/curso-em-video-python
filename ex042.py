reta1 = float(input('Informe a reta 1:'))
reta2 = float(input('Informe a reta 2:'))
reta3 = float(input('Informe a reta 3:'))

podeFormarTriangulo = ''

if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2):
    podeFormarTriangulo = 1
    print('As retas PODEM formar um triângulo.')
else:
    podeFormarTriangulo = 0
    print('As retas NÃO PODEM formar um triângulo.')
if podeFormarTriangulo == 1:
    if reta1 == reta2 == reta3:
        print('O triângulo é EQUILÁTERO.')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('O triângulo é ESCALENO.')
    #elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        #print('O triângulo é ISÓSCELES.')
    else:
        print('O triângulo é ISÓSCELES.')
