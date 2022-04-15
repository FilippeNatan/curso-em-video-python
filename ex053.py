frase = str(input('Informe uma frase para saber se é um palíndromo: '))
fraseInvertidaUpper = frase.replace(" ","").upper()[::-1]
fraseUpper = frase.replace(" ", "").upper() #transforma todas as letras em maíusculo para comparar abaixo
if(fraseInvertidaUpper == fraseUpper):
    print('A frase: {} ao contrário e sem espaços é {}.'.format(frase, fraseInvertidaUpper))
    print('Portanto é um palíndromo.')
else:
    print('A frase: {} ao contrário e sem espaços é {}.'.format(frase, fraseInvertidaUpper))
    print('Portanto não é um palíndromo.')
