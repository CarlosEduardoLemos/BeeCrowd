# Entrada de hora inicial, minuto inicial, hora final e minuto final
h_inicial, m_inicial, h_final, m_final = map(int, input().split())

# Converte as horas e minutos para minutos totais
inicio_total = h_inicial * 60 + m_inicial
final_total = h_final * 60 + m_final

# Calcula a duração do jogo em minutos
if final_total > inicio_total:
    duracao_total = final_total - inicio_total
else:
    duracao_total = (24 * 60 - inicio_total) + final_total

# Converte os minutos totais para horas e minutos
duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

# Exibe o resultado
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
