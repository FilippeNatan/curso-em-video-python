n = p = 0
while n >= 0:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        break
    for t in range(1, 10):
        p = n * t
        print(f'{n} x {t} = {p}')
print('TABUADA ENCERRADA! Não multiplicamos negativos aqui! Volte sempre!')
