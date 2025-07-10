n = int(input("Quantos números você vai digitar? "))
vet = [0 for x in range(n)]
print()

for i in range(0,n):
    vet[i] = int(input("Digite um número: "))
print()

print("NÚMEROS PARES:")
cont = 0
for i in range(0,n):
    if vet[i] % 2 == 0:
        cont = cont + 1
        print(vet[i], end= " ")
print()
print()
print(f"QUANTIDADE DE PARES = {cont}")