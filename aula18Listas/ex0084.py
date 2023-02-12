dado = []
pessoas = []
maior_peso = menor_peso = 0

while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dado[1]
    else:
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:
            menor_peso = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    continuar = input("Quer continuar? [S/N]: ")
    if continuar in "Nn":
        break

print(f"Você registrou {len(pessoas)} pessoas")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"O maior peso é {maior_peso}kg de {p[0]}",)
    if p[1] == menor_peso:
        print(f"O menor peso é {menor_peso}kg de {p[0]}")
