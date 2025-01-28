# Entrada de dois valores inteiros A e B
A, B = map(int, input().split())

# Verifica se são múltiplos
if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
