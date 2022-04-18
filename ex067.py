while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        break
    for t in range(1, 11):
        p = n * t
        print(f'{n} x {t} = {p}')
print('TABUADA ENCERRADA! Não multiplicamos negativos aqui! Volte sempre!')
