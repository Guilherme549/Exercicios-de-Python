n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))


try:
    print(n1/n2)
except: # se tiver algum erro ele executa esta linha
    print("Não consegui")
finally: # o finally sempre sera executado
    print("Finalizado")
