def calcular_media_ponderada(a, b, peso_a=3.5, peso_b=7.5):
    #Calcula a média ponderada de dois valores com pesos específicos.
    return (peso_a * a + peso_b * b) / (peso_a + peso_b)

def main():
    # Solicita os valores ao usuário
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    
    # Calcula a média ponderada dos valores
    media = calcular_media_ponderada(a, b)
    
    # Exibe o resultado
    print(f"MEDIA = {media:.5f}")

if __name__ == "__main__":
    main()