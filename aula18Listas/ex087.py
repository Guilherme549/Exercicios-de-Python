matriz = [[], [], []]
pares = []
soma_terceira_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f"Digite um valor para [{l}, {c}]: "))
        matriz[l].append(valor)
        if valor % 2 == 0:
            pares.append(valor)
        if c == 2:
            soma_terceira_coluna += valor
        if l == 1:
            maior_valor_segunda_linha = max(matriz[1])
for l, v in enumerate(matriz):
    for c in range(0, 3):
        print(f"[ {v[c]} ]", end="")
        if c == 2:
            print()
print("-="*20)
print(f"A soma dos numeros pares é {sum(pares)}")
print(f"A soma da terceira coluna é {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é {maior_valor_segunda_linha}")
print("-="*20)
