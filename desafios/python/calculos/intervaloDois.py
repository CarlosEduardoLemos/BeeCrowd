# Leitura do número de entradas
numero_entradas = int(input("Digite o número de entradas: "))

# Inicialização dos contadores
contador_dentro_intervalo = 0
contador_fora_intervalo = 0

# Loop para leitura e contagem dos números dentro e fora do intervalo [10, 20]
for _ in range(numero_entradas):
    numero = int(input("Digite um número: "))
    if 10 <= numero <= 20:
        contador_dentro_intervalo += 1
    else:
        contador_fora_intervalo += 1

# Impressão dos resultados
print(f"{contador_dentro_intervalo} in")
print(f"{contador_fora_intervalo} out")