count_pares = 0
count_impares = 0
count_positivos = 0
count_negativos = 0

for _ in range(5):
    num = int(input())
    if num % 2 == 0:
        count_pares += 1
    else:
        count_impares += 1
    if num > 0:
        count_positivos += 1
    elif num < 0:
        count_negativos += 1

print(f"{count_pares} valor(es) par(es)")
print(f"{count_impares} valor(es) impar(es)")
print(f"{count_positivos} valor(es) positivo(s)")
print(f"{count_negativos} valor(es) negativo(s)")
