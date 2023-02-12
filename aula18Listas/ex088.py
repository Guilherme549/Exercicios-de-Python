import random
import time

print("-" * 20)
print("    MEGA SENA    ")
print("-" * 20)
numerosDaMega = []

jogos = []
numeros = 0
tamanho = int(input("Quantos jogos você quer Fazer?: "))
print("-" * 20)
print(f"Sorteando {tamanho} jogos")
print("-" * 20)
time.sleep(1)

for l in range(0, tamanho):  # Define qual o tamanho da lista, pegando como valor a quantidade de jogos que o usuario definiu
    numerosDaMega.append(jogos[:])
    for v in range(0, 6):  # Com este loop é definido que serão sorteados 6 numeros por jogos
        if numeros not in numerosDaMega:
            numeros = random.randint(1, 60)
            numerosDaMega[l].append(numeros)

    print(f"Jogo {l+1}: {numerosDaMega[l]}")
    time.sleep(1)
