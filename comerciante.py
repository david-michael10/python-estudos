n = int(input("Serão digitados dados de quantos produtos? "))
nomes = [0 for x in range(n)]
p_c = [0 for x in range(n)]
p_v = [0 for x in range(n)]
print()

soma_c = 0
soma_v = 0
for i in range(0, n):
    print(f"Produto {i+1}:")
    nomes[i] = input("Nome: ")
    p_c[i] = float(input("Preço de Compra: "))
    soma_c = soma_c + p_c[i]
    p_v[i] = float(input("Preço de Venda: "))
    soma_v = soma_v + p_v[i]
    print()

pct = 0
menor_10 = 0
entre_10_20 = 0
acima_20 = 0
for i in range(0, n):
    pct = (p_v[i] * 100 / p_c[i]) - 100
    if pct < 10:
        menor_10 = menor_10 + 1
    elif pct >= 10 and pct < 20:
        entre_10_20 = entre_10_20 + 1
    else:
        acima_20 = acima_20 + 1

print("RELATÓRIO:")
print(f"Lucro abaixo de 10%: {menor_10}")
print(f"Lucro entre 10% e 20%: {entre_10_20}")
print(f"Lucro acima de 20%: {acima_20}")
print()
print(f"Valor total de compra: {soma_c:.2f}")
print(f"Valor total de venda: {soma_v:.2f}")
lucro_total = soma_v - soma_c
print(f"Lucro total: {lucro_total:.2f}")