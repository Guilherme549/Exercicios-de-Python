pessoas = dict()
dado = list()
media = list()
mulheres = list()
while True:
    pessoas["nome"] = (str(input("Nome: ")))
    pessoas["sexo"] = (str(input("Sexo: [M/F] ")))
    while pessoas["sexo"] not in "MF":
        pessoas["sexo"] = (str(input("Sexo: [M/F] "))).upper()
    pessoas["idade"] = (int(input("Idade: ")))
    if "F" in pessoas["sexo"] or "f" in pessoas["sexo"]:
        mulheres.append(pessoas["nome"])
    dado.append(pessoas.copy())
    media.append(pessoas["idade"])
    continuar = input("Quer continuar? [S/N]: ")
    if continuar in "Nn":
        media = sum(media) / len(media)
        break

print("-=" * 30)
print(f" - O grupo tem {len(dado)} pessoas.")
print(f" - A média de idade é de {media} anos.")
if len(mulheres) == 0:
    print(f" - As mulheres cadastradas foram: 0")
else:
    print(f" - As mulheres cadastradas foram: {mulheres}")
print(f" - Lista de pessoas que estão acima da média: ")

for p, v in enumerate(dado):
    if dado[p]['idade'] > media:
        print(
            f"nome = {dado[p]['nome']}; sexo = {dado[p]['sexo']}; idade = {dado[p]['idade']}")
print("<< ENCERRADO >>")
