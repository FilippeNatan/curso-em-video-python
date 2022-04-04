lado1 = float(input('Informe o primeiro lado:\n'))
lado2 = float(input('Informe o segundo lado:\n'))
lado3 = float(input('Informe o terceiro lado:\n'))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print('Você pode formar um triângulo com essas retas!')
else:
    print('Você não pode formar um triângulo com essas retas!')