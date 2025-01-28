def calcular_media_ponderada(a, b, c, peso_a=2, peso_b=3, peso_c=5):
    """Calcula a média ponderada de três valores com pesos específicos."""
    return (peso_a * a + peso_b * b + peso_c * c) / (peso_a + peso_b + peso_c)

def main():
    # Solicita os valores ao usuário
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    
    # Calcula a média ponderada dos valores
    media = calcular_media_ponderada(a, b, c)
    
    # Exibe o resultado
    print(f"MEDIA = {media:.1f}")

if __name__ == "__main__":
    main()