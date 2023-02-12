def contador(inicio, fim, passo):
    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if fim > inicio and passo > 0:
        for c in range(inicio, fim+1, passo):
            print(c, end=" ")
        print("FIM!")
    if fim < inicio and passo < 0:
        for c in range(inicio, fim+1, passo):
            print(c, end=" ")
        print("FIM!")
    if fim < inicio and passo > 0:
        for c in range(inicio, fim-1, -passo):
            print(c, end=" ")
        print("FIM!")
    if passo == 0 and fim > inicio:
        for c in range(inicio, fim+1, 1):
            print(c, end=" ")
        print("FIM!")
    if passo == 0 and passo <= 0:
        for c in range(inicio, fim-1, -1):
            print(c, end=" ")


contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
