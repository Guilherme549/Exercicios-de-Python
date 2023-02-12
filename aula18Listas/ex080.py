# faça um programa usando em listas os comandos append, insert, pop, remove del, extend, clear,
# index, count, sort, reverse, copy
resposta = 0
lista = []

adicionar = int(input("Digite um numero inteiro: "))

while resposta <= 3:
    lista.append(adicionar)
    resposta = int(input(
        "O que vc quer fazer?\n1-adicionar novo numero \n2-remover algum numero \n3-remover todos os numeros\n4-sair\nResposta: "))
    if resposta == 1:
        adicionar = int(input("Digite um numero inteiro: "))
        lista.append(adicionar)
        resposta = 0
    if resposta == 2:
        print(f"Os numeros adicionados são {lista}")
        remover = (input("Qual numero quer remover?"))
        lista.remove(remover)
        print(
            f"O numero {remover} foi removido com sucesso os numeros restantes são {lista}")
        resposta = 0
    if resposta == 3:
        lista.clear()
        print("Numeros removidos com sucesso!")
print("Vc saiu...")
print(f"Os numeros adicionados foram {lista} ")
