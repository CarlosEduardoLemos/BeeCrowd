# Leitura do código do item e da quantidade
codigo_item, quantidade = map(int, input("Digite o código do item e a quantidade separados por espaço: ").split())

# Determinação do preço com base no código do item
if codigo_item == 1:
    preco = 4.00 * quantidade
elif codigo_item == 2:
    preco = 4.50 * quantidade
elif codigo_item == 3:
    preco = 5.00 * quantidade
elif codigo_item == 4:
    preco = 2.00 * quantidade
elif codigo_item == 5:
    preco = 1.50 * quantidade

# Impressão do valor total
print(f"Total: R$ {preco:.2f}")