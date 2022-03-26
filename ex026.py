frase = str(input('Digite uma frase qualquer: ')).strip()
numLetraA = frase.lower().count('a')
primeiraOcorrencia = frase.lower().find('a')+1
ultimaOcorrencia = frase.lower().rfind('a')+1
print('A letra "A" aparece {} vez(es) na frase. A primeira posição é {}. A última posição é {}.'
      .format(numLetraA, primeiraOcorrencia, ultimaOcorrencia))
