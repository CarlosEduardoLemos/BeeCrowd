# Inicialização do contador de números pares
contador_pares = 0

# Loop para leitura e contagem dos números pares entre 5 entradas
for _ in range(5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        contador_pares += 1

# Impressão do resultado
print(f"{contador_pares} valores pares")