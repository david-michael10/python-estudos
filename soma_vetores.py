n = int(input("Quantos valores vai ter cada vetor? "))
a = [0 for x in range(n)]
b = [0 for x in range(n)]
c = [0 for x in range(n)]

print("Digite os valores de A:")
for i in range(0, n):
    a[i] = float(input())
print()

print("Digite os valores de B: ")
for i in range(0,n):
    b[i] = float(input())
print()

for i in range(0, n):
    c[i] = a[i] + b[i]
print("VETOR RESULTANTE: ")
for i in range(0,n):
    print(c[i])