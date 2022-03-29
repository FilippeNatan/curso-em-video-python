velocidadeDoCarro = float(input('Informe a velocidade do carro:'))
velocidadeMaxima = float(80)
valorDaMulta = 7.00 * (velocidadeDoCarro - velocidadeMaxima)

if velocidadeDoCarro > velocidadeMaxima:
    print('Você foi multado gafanhoto!\nO valor da multa é: R$ {:.2f}'.format(valorDaMulta))
else:
    print('Dentro da velocidade permitida.')
