# Leitura dos valores do primeiro item
entrada_item1 = input("Digite o código, quantidade e valor do primeiro item: ").split(' ')
codigo_item1 = int(entrada_item1[0])
quantidade_item1 = int(entrada_item1[1])
valor_item1 = float(entrada_item1[2])

# Leitura dos valores do segundo item
entrada_item2 = input("Digite o código, quantidade e valor do segundo item: ").split(' ')
codigo_item2 = int(entrada_item2[0])
quantidade_item2 = int(entrada_item2[1])
valor_item2 = float(entrada_item2[2])

# Cálculo do valor total a pagar
valor_total = (quantidade_item1 * valor_item1) + (quantidade_item2 * valor_item2)

# Impressão do resultado
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")