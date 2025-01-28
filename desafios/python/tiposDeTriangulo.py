# Entrada de três valores de ponto flutuante A, B e C
A, B, C = map(float, input().split())

# Ordena os lados em ordem decrescente
lados = sorted([A, B, C], reverse=True)
A, B, C = lados[0], lados[1], lados[2]

# Verifica se os valores formam um triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Verifica o tipo de triângulo quanto aos ângulos
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    # Verifica o tipo de triângulo quanto aos lados
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
