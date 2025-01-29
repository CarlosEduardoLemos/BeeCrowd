maior = 0
posicao = 0

for i in range(1, 101):  # Lendo 100 números
    num = int(input())
    
    if num > maior:
        maior = num
        posicao = i  # A posição é baseada na entrada (1 a 100)

print(maior)
print(posicao)
