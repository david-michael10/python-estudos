n = int(input("Quantos casos você vai digitar? "))

for i in range(0,n):
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    if denominador == 0:
        print("IMPOSSÍVEL CALCULAR")
        print()
    else:
        divisao = numerador / denominador
        print(f"DIVISÃO = {divisao:.2f}")
        print()