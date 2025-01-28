def ler_lados():
    #Lê três valores de ponto flutuante e retorna-os como uma tupla.
    return map(float, input().split())

def forma_triangulo(A, B, C):
    #Verifica se os valores A, B e C formam um triângulo.
    return A + B > C and A + C > B and B + C > A

def calcular_perimetro(A, B, C):
    #Calcula o perímetro do triângulo.
    return A + B + C

def calcular_area_trapezio(A, B, C):
    #Calcula a área do trapézio.
    return ((A + B) * C) / 2

def main():
    # Entrada dos valores reais A, B e C
    A, B, C = ler_lados()

    # Verifica se os valores formam um triângulo
    if forma_triangulo(A, B, C):
        # Calcula e imprime o perímetro do triângulo
        perimetro = calcular_perimetro(A, B, C)
        print(f"Perimetro = {perimetro:.1f}")
    else:
        # Calcula e imprime a área do trapézio
        area = calcular_area_trapezio(A, B, C)
        print(f"Area = {area:.1f}")

if __name__ == "__main__":
    main()