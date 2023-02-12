import time


def PyHelp():
    while True:
        time.sleep(1)
        titulo = "SISTEMA DE AJUDA PyHELP"
        print("~" * len(titulo))
        print(titulo)
        print("~" * len(titulo))
        func = input("Função ou biblioteca > ")
        if func in 'fim':
            time.sleep(1)
            titulo = "ATÉ LOGO!"
            print("~" * len(titulo))
            print(titulo)
            print("~" * len(titulo))
            time.sleep(1)
            break
        t1 = f"ACESSANDO MANUAL DO COMANDO {func}"

        print("~" * len(t1))
        print(t1)
        print("~" * len(t1))
        time.sleep(1)
        print(help(func))


PyHelp()
