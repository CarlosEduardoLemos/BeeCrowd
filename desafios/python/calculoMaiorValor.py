# Função lambda para calcular o maior de dois números
calcular_maior = lambda a, b: (a + b + abs(a - b)) // 2

# Leitura dos valores de A, B e C
a, b, c = [int(x) for x in input("Digite os valores de A, B e C separados por espaço: ").split(' ')]

# Cálculo do maior valor entre A, B e C
maior_valor = calcular_maior(a, calcular_maior(b, c))

# Impressão do resultado
print(f"{maior_valor} eh o maior")