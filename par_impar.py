n = int(input("Quantos números você vai digitar? "))
for i in range(0,n):
    x = int(input("Digite um número: "))
    if x > 0 and x % 2 == 0:
        print("PAR POSITIVO")
    elif x < 0 and x % 2 == 0:
        print("PAR NEGATIVO")
    elif x > 0 and x % 2 != 0:
        print("ÍMPAR POSITIVO")
    elif x < 0 and x % 2 != 0:
        print("ÍMPAR NEGATIVO")
    else:
        print("NULO")