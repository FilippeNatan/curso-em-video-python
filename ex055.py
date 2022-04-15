numPessoas = 5
arrPeso = []

for contador in range(numPessoas):
    peso = int(input('Informe o peso de {}° pessoa: '.format(contador+1)))#gambi
    # tentei iniciar a variavel com um, mas não deu certo
    arrPeso.append(peso)
print('O maior peso é {} Kg e menor peso é {} Kg'.format(max(arrPeso, key=int),min(arrPeso, key=int)))
