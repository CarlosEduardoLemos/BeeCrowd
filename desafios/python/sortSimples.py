def ler_valores():
    # Lê três valores inteiros e retorna-os como uma lista
    return list(map(int, input("Digite três valores inteiros separados por espaço: ").split()))

def exibir_valores(valores):
    # Exibe os valores, um por linha
    for valor in valores:
        print(valor)

def main():
    # Lê os valores de entrada
    valores = ler_valores()

    # Cria uma cópia dos valores para preservar a ordem original
    valores_originais = valores[:]

    # Ordena os valores em ordem crescente
    valores.sort()

    # Exibe os valores em ordem crescente
    exibir_valores(valores)

    # Linha em branco
    print()

    # Exibe os valores na sequência como foram lidos
    exibir_valores(valores_originais)

if __name__ == "__main__":
    main()