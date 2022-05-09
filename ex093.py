dadosJogador = {}
listaGols = []

dadosJogador['nome'] = str(input('Nome do jogador: '))
numeroPartidas = int(input('Quantas partidas o jogador jogou? '))
for n in range(1, numeroPartidas+1):
    listaGols.append(int(input(f'Quantos gols na partida {n}? ')))
dadosJogador['gols'] = listaGols
dadosJogador['total'] = sum(listaGols)
print('-=-'*20)
print(dadosJogador)
print('-=-'*20)
for i, v in dadosJogador.items():
    print(f'O campo {i} tem o valor {v}.')
print('-=-'*20)
print(f'O jogador {dadosJogador["nome"]} jogou {numeroPartidas} partidas.')
for i, v in enumerate(listaGols):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dadosJogador["total"]} gols.')
