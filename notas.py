nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota = nota1 + nota2
print()
print(f"NOTA FINAL = {nota:.1f}")

if nota < 60:
    print("REPROVADO")
else:
    print("APROVADO")