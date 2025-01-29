N = int(input())

for _ in range(N):
    X = int(input())
    
    if X == 0:
        print("NULL")
    else:
        result = "EVEN" if X % 2 == 0 else "ODD"
        result += " POSITIVE" if X > 0 else " NEGATIVE"
        print(result)