print("Digite as 3 distâncias: ")
a = float(input())
b = float(input())
c = float(input())

if a > b and a > c:
    print(f"MAIOR DISTÂNCIA: {a:.2f}")
elif b > c:
    print(f"MAIOR DISTÂNCIA: {b:.2f}")
else:
    print(f"MAIOR DISTÂNCIA: {c:.2f}")