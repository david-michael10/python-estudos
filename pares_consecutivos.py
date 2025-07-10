x = 1
while x != 0:
    x = int(input("Digite um número inteiro: "))
    if x != 0:
        soma = 0
        for i in range(0,10):
            if x % 2 == 0:
                soma = soma + x
            x = x + 1
        print(f"SOMA = {soma}")