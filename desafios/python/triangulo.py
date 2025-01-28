# Entrada dos valores reais A, B e C
A, B, C = map(float, input().split())

# Verifica se os valores formam um triângulo
if A + B > C and A + C > B and B + C > A:
    # Calcula o perímetro do triângulo
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Calcula a área do trapézio
    area = ((A + B) * C) / 2
    print(f"Area = {area:.1f}")
