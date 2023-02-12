import random
import time

numeros = []


def sorteia():
    print("Sorteando 5 valores na lista: ", end="")
    for c in range(0, 5):
        numeros.append(random.randint(1, 10))
        print(f"{numeros[c]}", end=" ", flush=True)
        time.sleep(0.5)
    print("PRONTO!")


def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f"Somando os valores pares de {numeros}, temos {soma}")


sorteia()
somaPar()
