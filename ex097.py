def escrever(titulo):
    tamanho = len(titulo)
    print('=-=' * tamanho)
    print(f'{titulo:^{tamanho*3}}')
    print('=-=' * tamanho)

titulo = str(input('Informe o título desejado: '))
escrever(titulo)
