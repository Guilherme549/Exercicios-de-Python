def linha(a):
    return print("-" * 30), print(a), print("-" * 30)


linha("Guilherme")


def contador(* num):  # metodo de empacotar parametros. Retorna uma tupla
    print(num)


contador(5, 6, 7, 4)


def dobra(lst):  # tambem posso usar listas como parametro
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [5, 6, 7, 8, 3, 2]
dobra(valores)
print(valores)
