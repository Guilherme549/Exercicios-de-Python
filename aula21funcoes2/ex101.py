from datetime import datetime


def voto(ano):
    idade = datetime.now().year - ano
    if idade >= 18 and idade < 65:
        print(f"Com {idade} anos: VOTO OBRIGATÓRIO.")
    if idade < 18:
        print(f"Com {idade} anos: NÃO VOTA.")
    if idade > 65:
        print(f"Com {idade} anos: VOTO OPCIONAL.")


ano = int(input("Em que ano você nasceu? "))
print("-" * 30)
voto(ano)
