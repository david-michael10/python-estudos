n = int(input("Quantas pessoas serão digitadas? "))
alturas = [0 for x in range(n)]
generos = [0 for x in range(n)]
print()

for i in range(0,n):
    alturas[i] = float(input(f"Altura da {i+1}a pessoa: "))
    generos[i] = input(f"Gênero da {i+1}a pessoa (M/F): ")
    print()

menor_altura = alturas[0]
for i in range(1,n):
    if alturas[i] < menor_altura:
        menor_altura = alturas[i]
print(f"MENOR ALTURA = {menor_altura}")

maior_altura = alturas[0]
for i in range(1,n):
    if alturas[i] > maior_altura:
        maior_altura = alturas[i]
print(f"MAIOR ALTURA = {maior_altura}")
print()

cont_m = 0
soma_m = 0
for i in range(0,n):
    if generos[i] == "f":
        cont_m = cont_m + 1
        soma_m = soma_m + alturas[i]
media_m = soma_m / cont_m
print(f"MÉDIA DE ALTURA DAS MULHERES = {media_m:.2f}")

cont_h = 0
for i in range(0,n):
    if generos[i] == "m":
        cont_h = cont_h + 1
print(f"NÚMERO DE HOMENS = {cont_h}")