n = int(input("Quantos números você vai digitar? "))
vet = [0 for x in range(n)]
print()

for i in range(0, n):
    vet[i] = float(input("Digite um número: "))
print()

print("VALORES = ", end= " ")
for i in range(0, n):
    print(f"{vet[i]:.1f}", end= " ")
print()

soma = 0
for i in range(0, n):
    soma = soma + vet[i]
print(f"SOMA = {soma:.2f}")

media = soma / n
print(f"MÉDIA = {media:.2f}")