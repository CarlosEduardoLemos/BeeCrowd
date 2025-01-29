import math

# Função para calcular o MDC
def mdc(a, b):
    return math.gcd(a, b)

# Entrada
N = int(input())  # Número de casos de teste

# Processamento e saída
for _ in range(N):
    F1, F2 = map(int, input().split())
    print(mdc(F1, F2))
