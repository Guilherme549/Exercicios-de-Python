matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f"Digite um valor para [{l}, {c}]: ")))
for l, v in enumerate(matriz):
    for c in range(0, 3):
        print(f"[ {v[c]} ]", end="")
        if c == 2:
            print()
