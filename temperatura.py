temp = input("Você vai digitar a temperatura em qual escala? (C/F): ")
if temp == "f":
    fah = float(input("Digite a temperatura em Fahrenheit: "))
    para_celsius = (fah - 32) * 5 / 9
    print(f"Temperatura aproximada em Celsius: {para_celsius:.2f}")
elif temp == "c":
    fah = float(input("Digite a temperatura em Celsius: "))
    para_fah = (fah * 9) / 5 + 32
    print(f"Temperatura aproximada em Fahrenheit: {para_fah:.2f}")