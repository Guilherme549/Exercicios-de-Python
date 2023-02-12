jogador = dict()
levantamento = list()
gols = list()
while True:
    jogador["nome"] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for p in range(0, partidas):
        gols.append(int(input(f"Quantos gols na partida {p}? ")))
        jogador["gols"] = gols[:]
        jogador["total"] = sum(gols)
    gols.clear()
    levantamento.append(jogador.copy())
    continuar = input("Quer continuar? [S/N]: ")
    if continuar in "Nn":
        break
print("-=" * 40)
print("cod    nome    gols    total")
for p, v in enumerate(levantamento):
    print(
        f"{p}    {levantamento[p]['nome']}    {levantamento[p]['gols']}    {levantamento[p]['total']}")
print("-=" * 40)
valor = 0
while valor < 999:
    for p, v in enumerate(levantamento):
        valor = int(input("Mostrar dado de qual jogador? (999 interrompe): "))
        if valor == p:
            print("-=" * 40)
            print(f"-- LEVANTAMENTO DO JOGADOR {levantamento[p]['nome']}:")
            for c in range(0, len(levantamento[p]['gols'])):
                print(
                    f"    No jogo {c+1} fez {levantamento[p]['gols'][c]} gol.")
        else:
            print("-=" * 40)
            print(
                f"ERRO! não existe jogador com código {valor}! tente novamente:")
            print("-=" * 40)
