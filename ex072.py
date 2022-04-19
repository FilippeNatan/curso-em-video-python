tuplaNumeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
                'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinte', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numeroEscolhido = int(input('Escolha um número de 0 a 20: '))
while numeroEscolhido not in range(0, 21):
    numeroEscolhido = int(input('Opção inválida. Escolha um número de 0 a 20: '))
print(f'O número escolhido foi o {tuplaNumeros[numeroEscolhido]}.')
