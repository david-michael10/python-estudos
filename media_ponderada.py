n = int(input("Quantos casos você vai digitar? "))

for i in range(0, n):
    print("Digite 3 números:")
    np1 = float(input())
    np1 = np1 * 2
    np2 = float(input())
    np2 = np2 * 3
    np3 = float(input())
    np3 = np3 * 5
    media = (np1 + np2 + np3) / (2 + 3 + 5)
    print(f"MÉDIA = {media:.1f}")