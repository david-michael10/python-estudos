n = int(input("Quantos números você vai digitar? "))
vet = [0 for x in range(0,n)]
print()

for i in range(0,n):
    vet[i] = float(input("Digite um número: "))
print()

maior = vet[0]
pos = 0
for i in range(1,n):
    if vet[i] > maior:
        maior = vet[i]
        pos = i
print(f"MAIOR VALOR = {maior:.1f}")
print(f"POSIÇÃO DO MAIOR VALOR = {pos}")