alunos = dict()

alunos["nome"] = str(input("Nome: "))
alunos["media"] = float(input("Média: "))

if alunos["media"] >= 6 or alunos["media"] >= 60:
    print(f"A média é igual a {alunos['media']}")
    print("Aprovado")
else:
    print(f"A média é igual a {alunos['media']}")
    print("Reprovado")
