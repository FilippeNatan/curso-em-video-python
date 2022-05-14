def titulo(titulo):
    print(10*'=-=')
    print(f'{titulo:^30}')
    print(10*'=-=')


def area(l, c):
    area = l * c
    print(f'A área de um terreno {l} X {c} é de {area}m².')

titulo('Controle de Terrenos')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
