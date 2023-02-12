dado = {"nome": "Guilherme", "idade": 19, "sexo": "M"}


print(dado.values())  # imprime o valor
print(dado.keys())  # imprime a chave
print(dado.items())  # imprime a chave e o valor


for k, v in dado.items():  # este loop é como se fosse o enumerate mas os serve para dicionarios
    print(f"O {k} é {v}")


estado = dict()
brasil = list()

for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
