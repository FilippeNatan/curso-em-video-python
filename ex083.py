abrindo = 0; fechando = 0
expressao = (str(input('Digite uma expressão: ')))
for n in expressao:
    if n in '(':
        abrindo += 1
    elif n in ')':
        fechando += 1
if abrindo == fechando:
    print('Sua expressão é válida!')
elif abrindo != fechando:
    print('Sua expressão é inválida!')
