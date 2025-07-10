import math
base = float(input("Base do retângulo: "))
altura = float(input("Altura do retângulo: "))
area = base * altura
perimetro = (2 * base) + (2 * altura)
diagonal = math.sqrt((base ** 2) + (altura ** 2))
print()

print(f"ÁREA = {area:.4f}")
print(f"PERÍMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")