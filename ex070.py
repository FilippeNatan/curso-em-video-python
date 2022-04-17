nomeProduto = 'Nenhum'; precoProduto = 0; querContinuar = 'S'; totalGasto = 0; produtosMais1000 = 0;
primeiraVez = True; nomeMaisBarato = 'Nenhum'; precoMaisBarato = 0

while True:
    nomeProduto = str(input('Informe o nome do produto: ')).strip()
    while nomeProduto == '':
        nomeProduto = str(input('Informe o nome do produto: ')).strip()
    precoProduto = int(input('Informe o preço do produto: '))
    while precoProduto < 0:
        precoProduto = int(input('Informe o preço do produto: '))
    totalGasto += precoProduto
    if precoProduto > 1000:
        produtosMais1000 += 1
    if primeiraVez == True:
        primeiraVez == False
        nomeMaisBarato = nomeProduto
        precoMaisBarato = precoProduto
    if precoProduto < precoMaisBarato:
        nomeMaisBarato = nomeProduto
        precoMaisBarato = precoProduto
    querContinuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while querContinuar not in 'SNsn':
        querContinuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if querContinuar in 'Nn':
        break
print(f'O total gasto foi de R$ {totalGasto},00\n'
      f'{produtosMais1000} produto(s) custam mais de R$ 1000,00\n'
      f'{nomeMaisBarato} é o produto mais barato e seu preço é R$ {precoMaisBarato},00')
