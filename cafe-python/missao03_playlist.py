# =====================================================
#  CAFÉ PYTHON - Missão 3: A playlist da loja
# =====================================================
# A loja toca música o dia todo. A dona quer saber quanto tempo
# dura a playlist inteira, sem repetir nenhuma música.

quantidade_musicas = 1591
duracao_media_segundos = 197

# SUA MISSÃO
# 1. segundos_totais = quantidade_musicas vezes duracao_media_segundos
# 2. Transforme segundos_totais em dias, horas e minutos:
#    - dias    = quantos dias inteiros cabem (1 dia = 86400 segundos)
#    - horas   = quantas horas inteiras SOBRAM depois de tirar os dias (1 hora = 3600 s)
#    - minutos = quantos minutos inteiros SOBRAM depois de tirar as horas
#    Dica: // diz "quantos cabem" e % diz "quanto sobra".

# ---- escreva seu código abaixo desta linha ----

dias = 0
horas = 0
minutos = 0

# ---- não mexa na linha abaixo ----
print("FLAG{" + str(dias) + "d" + str(horas) + "h" + str(minutos) + "m}")
