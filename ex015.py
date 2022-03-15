diasAluguel=(int(input('Por quantos dias o carro foi alugado?')))
quilometrosRodados=(float(input('Quantos Km foram percorridos?')))
print('O valor total a pagar é R$ {:.2f}.'.format((diasAluguel*60)+(quilometrosRodados*0.15)))
