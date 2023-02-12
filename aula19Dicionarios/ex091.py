import random
import time

cont = 1
dado = {"jogador1": random.randint(1, 6), "jogador2": random.randint(
    1, 6), "jogador3": random.randint(1, 6), "jogador4": random.randint(1, 6), }
time.sleep(1)
print("Valores sorteados:")
time.sleep(1)
for k, v in dado.items():
    print(f"  O {k} tirou {v}")
    time.sleep(1.5)
time.sleep(1.5)
print("Ranking do jogadores:")
time.sleep(1.5)
for jogador in sorted(dado, key=dado.get, reverse=True):
    print(f"  {cont}º lugar: {jogador} com {dado[jogador]}")
    cont += 1
    time.sleep(1.5)
