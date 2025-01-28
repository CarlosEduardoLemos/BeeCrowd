# Entrada: três valores inteiros
valores = list(map(int, input().split()))

# Cria uma cópia dos valores para preservar a ordem original
valores_originais = valores[:]

# Ordena os valores em ordem crescente
valores.sort()

# Exibe os valores em ordem crescente
for valor in valores:
    print(valor)

# Linha em branco
print()

# Exibe os valores na sequência como foram lidos
for valor in valores_originais:
    print(valor)
