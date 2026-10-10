# =====================================================
#  CAFÉ PYTHON - Missão 8 (DESAFIO FINAL): O fechamento do mês
# =====================================================
# A dona do Café & Letras precisa do relatório de vendas do mês.
# Os dados estão no arquivo vendas.csv. Deixe o vendas.csv NA MESMA PASTA deste arquivo.
#
# A primeira linha do arquivo é o cabeçalho (os nomes das colunas):
#   pedido;data;produto;quantidade;preco_unitario;status
# As outras linhas são os pedidos, por exemplo:
#   1042;2026-10-03;cappuccino;2;14.50;pago
#
# linha.strip().split(";") quebra a linha nos ";". Os pedaços ficam assim:
#   índice 0 -> número do pedido   "1042"
#   índice 2 -> produto            "cappuccino"
#   índice 3 -> quantidade         "2"      (texto! use int)
#   índice 4 -> preço unitário     "14.50"  (texto! use float)
#   índice 5 -> status             "pago" ou "cancelado"

from pathlib import Path

caminho = Path(__file__).parent / "vendas.csv"   # não mexa

# SUA MISSÃO: descubra
# 1. total_pedidos   -> quantos pedidos existem (NÃO conte o cabeçalho!)
# 2. cancelados      -> quantos pedidos foram cancelados
# 3. mais_vendido    -> o produto que aparece em MAIS pedidos pagos
# 4. maior_pedido    -> o número do pedido pago de MAIOR valor
#                       (valor = quantidade x preço unitário)
#
# Para ler o arquivo linha por linha:
#   with open(caminho, encoding="utf-8") as arquivo:
#       cabecalho = arquivo.readline()     # lê e pula a primeira linha
#       for linha in arquivo:
#           partes = linha.strip().split(";")
#           ...
#
# Dica para o item 3: junte numa lista o produto de cada pedido pago.
# Depois, para cada produto (sem repetir), use lista.count(produto).

# ---- escreva seu código abaixo desta linha ----

total_pedidos = 0
cancelados = 0
mais_vendido = ""
maior_pedido = ""

# ---- não mexa na linha abaixo ----
print("FLAG{" + str(total_pedidos) + "-" + str(cancelados) + "-" + mais_vendido + "-" + str(maior_pedido) + "}")
