salarioFuncionario = float(input('Informe o seu salário para saber o aumento:'))

salarioAlto = salarioFuncionario * 1.10

salarioBaixo = salarioFuncionario * 1.15

if salarioFuncionario > 1250:
    print('O seu salário será de R$ {:.2f}'.format(salarioAlto))
else:
    print('O seu salário será de R$ {:.2f}'.format(salarioBaixo))
