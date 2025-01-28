# Função para ler a hora inicial, minuto inicial, hora final e minuto final
def ler_horarios():
    # Lê a hora inicial, minuto inicial, hora final e minuto final
    return map(int, input().split())

# Função para converter horas e minutos para minutos totais
def converter_para_minutos(horas, minutos):
    # Converte horas e minutos para minutos totais
    return horas * 60 + minutos

# Função para calcular a duração do jogo em minutos
def calcular_duracao(inicio_total, final_total):
    # Calcula a duração do jogo em minutos
    if final_total > inicio_total:
        return final_total - inicio_total
    else:
        return (24 * 60 - inicio_total) + final_total

# Função para converter a duração total em minutos para horas e minutos
def converter_para_horas_minutos(duracao_total):
    # Converte a duração total em minutos para horas e minutos
    horas = duracao_total // 60
    minutos = duracao_total % 60
    return horas, minutos

def main():
    # Entrada de hora inicial, minuto inicial, hora final e minuto final
    h_inicial, m_inicial, h_final, m_final = ler_horarios()

    # Converte as horas e minutos para minutos totais
    inicio_total = converter_para_minutos(h_inicial, m_inicial)
    final_total = converter_para_minutos(h_final, m_final)

    # Calcula a duração do jogo em minutos
    duracao_total = calcular_duracao(inicio_total, final_total)

    # Converte os minutos totais para horas e minutos
    duracao_horas, duracao_minutos = converter_para_horas_minutos(duracao_total)

    # Exibe o resultado
    print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")

if __name__ == "__main__":
    main()