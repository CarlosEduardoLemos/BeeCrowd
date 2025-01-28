# Leitura do valor inteiro
valor = int(input("Digite um valor inteiro: "))

# Impressão do valor lido
print(valor)

# Cálculo e impressão da quantidade de notas de cada valor
print(f"{valor // 100} nota(s) de R$ 100,00")
valor %= 100
print(f"{valor // 50} nota(s) de R$ 50,00")
valor %= 50
print(f"{valor // 20} nota(s) de R$ 20,00")
valor %= 20
print(f"{valor // 10} nota(s) de R$ 10,00")
valor %= 10
print(f"{valor // 5} nota(s) de R$ 5,00")
valor %= 5
print(f"{valor // 2} nota(s) de R$ 2,00")
valor %= 2
print(f"{valor} nota(s) de R$ 1,00")