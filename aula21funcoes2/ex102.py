def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :para n: O numero a ser calculado.
    :para show: (opicional) para mostrar como foi feita a conta
    :retunr: não tem return
    """
    resultado = 1
    for c in range(n, 0, -1):
        resultado *= c
        if show == True:
            print(f"{c} x", end=" ")
    if show == False:
        print(f"{resultado}")
    else:
        print(f"= {resultado}")


fatorial(5, True)
help(fatorial)
