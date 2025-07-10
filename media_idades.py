print("Digite as idades:")
idades = int(input())
if idades < 0:
    print("IMPOSSÍVEL CALCULAR")
    cont = 0
else:
    media = 0
    soma = 0
    cont = 0
    while idades > 0:
        soma = soma + idades
        cont = cont + 1
        idades = int(input())
if cont != 0:
    media = soma / cont
    print(f"MÉDIA = {media:.2f}")