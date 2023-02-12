jogador = dict()
gols = list()
jogador["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for p in range(0, partidas):
    gols.append(int(input(f"Quantos gols na partida {p}? ")))
    jogador["gols"] = gols
    jogador["total"] = sum(gols)
print("-=" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}.")
print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for p, v in enumerate(gols):
    print(f"   => Na partida {p+1}, fez {v} gols.")
print(f"foi um total de {jogador['total']} gols.")
