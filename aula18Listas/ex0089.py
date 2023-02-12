boletim = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continuar = input("Quer continuar? [S/N]: ")
    if continuar in "Nn":
        break

print(f"No.     NOME     MÉDIA")
print("-" * 30)
for p, v in enumerate(boletim):
    print(f"{p}     {boletim[p][0]}     {boletim[p][2]}")

while True:
    for p, v in enumerate(boletim):
        mostrar_notas = int(
            input("Mostrar notas de qual aluno? (999 interrompe): "))
        if mostrar_notas == p:
            print(f"As notas de {boletim[p][0]} são {boletim[p][1]} ")
        if mostrar_notas == 999:
            exit()
