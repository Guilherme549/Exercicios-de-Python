def leiaInt(entrada):
    valor = str(input(entrada))
    while True:
        if valor.isnumeric():
            valor = int(valor)
            return valor
        else:
            print('\033[31mERRO! Digite um número inteiro.\033[m')
            valor = str(input(entrada))


n = leiaInt("Digite um numero inteiro: ")
print(f"Você acabou de digitar o número {n}.")
