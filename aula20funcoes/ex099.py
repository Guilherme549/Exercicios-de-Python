import time


def maior(* num):
    print("-=" * 20)
    print("Analisando valores passados...")
    cont = 0
    for c in num:
        print(c, end=" ", flush=True)
        cont += 1
        time.sleep(0.3)
    print(f"Foram informados {len(num)} ao todo")
    print(f"O maior valor é {cont}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
