nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Valor Inválido. Tente Novamente: "))
print()

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Valor Inválido. Tente Novamente: "))
print()

media = (nota1 + nota2) / 2
print(f"MÉDIA = {media:.2f}")