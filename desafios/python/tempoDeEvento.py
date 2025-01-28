# Função para converter um horário no formato hh:mm:ss para segundos
def horario_para_segundos(dia, hora, minuto, segundo):
    return (dia - 1) * 86400 + hora * 3600 + minuto * 60 + segundo

# Função para ler a entrada de data e hora
def ler_data_hora():
    dia = int(input().split()[1])
    hora, minuto, segundo = map(int, input().split(' : '))
    return dia, hora, minuto, segundo

# Função para calcular a diferença de tempo em dias, horas, minutos e segundos
def calcular_diferenca_tempo(inicio_segundos, fim_segundos):
    duracao_segundos = fim_segundos - inicio_segundos

    dias = duracao_segundos // 86400
    duracao_segundos %= 86400

    horas = duracao_segundos // 3600
    duracao_segundos %= 3600

    minutos = duracao_segundos // 60
    segundos = duracao_segundos % 60

    return dias, horas, minutos, segundos

# Leitura da entrada
dia_inicio, hora_inicio, minuto_inicio, segundo_inicio = ler_data_hora()
dia_fim, hora_fim, minuto_fim, segundo_fim = ler_data_hora()

# Conversão dos horários para segundos
inicio_segundos = horario_para_segundos(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio)
fim_segundos = horario_para_segundos(dia_fim, hora_fim, minuto_fim, segundo_fim)

# Cálculo da diferença em dias, horas, minutos e segundos
dias, horas, minutos, segundos = calcular_diferenca_tempo(inicio_segundos, fim_segundos)

# Exibição do resultado
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")