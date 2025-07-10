print("Digite 2 números: ")
x = int(input())
y = int(input())
if x > y:
    print("DECRESCENTE")
else:
    print("CRESCENTE")
print()

while x != y:
    print("Digite outros 2 números: ")
    x = int(input())
    y = int(input())
    if x != y:
        if x > y:
            print("DECRESCENTE")
            print()
        else:
            print("CRESCENTE")
            print()