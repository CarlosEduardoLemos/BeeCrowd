X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

soma = sum(num for num in range(X + 1, Y) if num % 2 != 0)

print(soma)
