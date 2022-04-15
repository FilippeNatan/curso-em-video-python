numPessoas = 5
arrPeso = []

for contador in range(1, numPessoas+1):#coloquei +1 pois o contador inicia em 0
    peso = int(input('Informe o peso de {}° pessoa: '.format(contador)))
    arrPeso.append(peso)
print('O maior peso é {} Kg e menor peso é {} Kg'.format(max(arrPeso, key=int),min(arrPeso, key=int)))
