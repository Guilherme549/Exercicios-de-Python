def contador(i, f, p):  # É Possivel fazer uma documentação da sua propia função usando 3 aspas duplas
    """
    ->faz uma contagem e mostra na tela.
    :para i: inicio da contagem
    :para f: fim da contagem
    :para p: passa a contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c}", end=" ")
        c += p
    print("FIM!")


help(contador)


def somar(a=0, b=0, c=0):  # parametros opcionais. se o usuario nao colocar nenhum parametro, automaticamante vai ser 0
    s = a+b+c
    print(f"A soma é {s}")


somar(2, 4, 3)
