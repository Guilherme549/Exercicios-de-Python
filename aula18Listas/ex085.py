numeros_par_e_impar = [[], []]
valor = 0

for v in range(1, 8):
    valor = int(input(f"Digite {v}º valor: "))
    if valor % 2 == 0:
        numeros_par_e_impar[0].append(valor)
    else:
        numeros_par_e_impar[1].append(valor)

print(
    f"Os valores pares digitados foram : {sorted(numeros_par_e_impar[0], key=int)}")
print(
    f"Os valores ímpares digitados foram {sorted(numeros_par_e_impar[1], key=int)}")
