largura = float(input("Largura do terreno: "))
comprimento = float(input("Comprimento do terreo: "))
valor_metro_quadrado = float(input("Valor do metro quadrado: "))
area = largura * comprimento
preco_terreno = valor_metro_quadrado * area
print()

print(f"Área do terreno: {area:.2f}")
print(f"Preço do terreno: {preco_terreno:.2f}")