from time import sleep
import emoji

print('Contagem regressiva para os fogos de artifício!')

for n in range(10, -1, -1):
    print(n)
    sleep(1)
print(emoji.emojize("Feliz Ano Novo! :sparkles:"))
