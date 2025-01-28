def ler_lados():
    """Lê três valores de ponto flutuante e retorna-os em uma lista ordenada decrescentemente."""
    A, B, C = map(float, input().split())
    return sorted([A, B, C], reverse=True)

def verificar_tipo_triangulo(A, B, C):
    """Verifica e imprime o tipo de triângulo baseado nos lados A, B e C."""
    if A >= B + C:
        print("NAO FORMA TRIANGULO")
    else:
        if A**2 == B**2 + C**2:
            print("TRIANGULO RETANGULO")
        if A**2 > B**2 + C**2:
            print("TRIANGULO OBTUSANGULO")
        if A**2 < B**2 + C**2:
            print("TRIANGULO ACUTANGULO")

        if A == B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")

def main():
    lados = ler_lados()
    A, B, C = lados[0], lados[1], lados[2]
    verificar_tipo_triangulo(A, B, C)

if __name__ == "__main__":
    main()