#  Crie um programa onde o usuário possa digitar vários
#  valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados,
#  em ordem crescente.


lista = []

while True:
    adicionar = int(input("Digite um numero inteiro: "))
    lista.append(adicionar)
    continuar = input("Quer continuar? [S/N]: ")
    if continuar in 'Nn':
        break

print(f"Os numeros que vc adicionou foram {lista}")
