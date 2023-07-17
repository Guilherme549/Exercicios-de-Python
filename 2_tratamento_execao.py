try:
    x = int(input("Digite um numero: "))
    print(5/x)
except ValueError:
    print("Digite um numero inteiro!")
except ZeroDivisionError:
    print("Não digite 0!")