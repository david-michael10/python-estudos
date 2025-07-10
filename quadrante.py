print("Digite os valores X e Y:")
x = int(input())
y = int(input())
while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("QUADRANTE Q1")
        print()
    elif x > 0 and y < 0:
        print("QUADRANTE Q4")
        print()
    elif x < 0 and y < 0:
        print("QUADRANTE Q3")
        print()
    else:
        print("QUADRANTE Q2")
        print()
    print("Digite os valores X e Y:")
    x = int(input())
    y = int(input())