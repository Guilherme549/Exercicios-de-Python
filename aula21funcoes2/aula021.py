def variavelGlobal():
    global a
    a = 3
    print(a)


a = 9
variavelGlobal()


def somar(a=0, b=0, c=0):
    s = a+b+c
    return s  # este retorno da funçaõ pode ser guardado dentro de uma varial o pode ser printando


resposta = somar(1, 2, 3)

print(resposta)
