from datetime import datetime

cadastro = dict()

cadastro["nome"] = str(input("Nome: "))
cadastro["nascimento"] = int(input("Ano de nascimento: "))
cadastro["idade"] = datetime.now().year - cadastro["nascimento"]
cadastro["ctps"] = int(input("Carteira de trabalho: (0 não tem): "))
if cadastro["ctps"] > 0:
    cadastro["contratacao"] = int(input("Ano de contratação: "))
    cadastro["aposentadoria"] = (
        cadastro["contratacao"] - cadastro["nascimento"]) + 35
    print("-=" * 30)
    for k, v in cadastro.items():
        print(f"{k} tem o valor de {v}")
    print("-=" * 30)
else:
    print("-=" * 30)
    for k, v in cadastro.items():
        print(f"{k} tem o valor de {v}")
print("-=" * 30)
