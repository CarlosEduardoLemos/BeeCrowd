# Leitura dos valores A, B, C e D
A, B, C, D = [int(x) for x in input("Digite os valores de A, B, C e D separados por espaço: ").strip().split(' ')]

# Verificação das condições e impressão do resultado
if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")