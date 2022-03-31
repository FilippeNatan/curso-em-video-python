distanciaViagem = float(input('Informe qual a distância da viagem em KM:\n'))
viagemCurta = distanciaViagem * 0.5
viagemLonga = distanciaViagem * 0.45
if distanciaViagem <= 200:
    print('Sua viagem custará R$ {:.2f}'.format(viagemCurta))
else:
    print('Sua viagem custará R$ {:.2f}'.format(viagemLonga))
