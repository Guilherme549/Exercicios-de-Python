def ficha(nome="<desconhecido>", gols=0):
    if nome == "":
        nome = "<desconhecido>"
    print(f"Jogador {nome} fez {gols} gols(s) no campeonato.")


nome = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
