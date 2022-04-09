nota1 = float(input('Informe a primera nota:'))
nota2 = float(input('Informe a segunda nota:'))
total = (nota1 + nota2)/2

if total < 5:
    print('A sua média final foi {}. Infelizmente REPROVADO!'.format(total))
elif total >= 5 and total < 6.9:
    print('A sua média final foi {}. Estude bastante para a RECUPERAÇÃO.'.format(total))
else:
    print('A sua média final foi {}, APROVADO. Boas férias!'.format(total))
