# =====================================================
#  CAFÉ PYTHON - Missão 2: Estoque de café
# =====================================================
# Os dados abaixo vieram de uma planilha do fornecedor.
# Por isso TODOS chegaram como texto (str), mesmo sendo números.

sacos = "17"
kg_por_saco = "48"
pacotes_de_cha = "6"
preco_por_pacote = "12.75"

# SUA MISSÃO
# 1. Converta cada valor para o tipo numérico certo:
#    - números inteiros  -> int()
#    - números com ponto -> float()
# 2. Calcule kg_total: quantos quilos de café existem somando todos os sacos.
# 3. Calcule valor_cha: quanto custam todos os pacotes de chá juntos.

# ---- escreva seu código abaixo desta linha ----

kg_total = 0
valor_cha = 0

# ---- não mexa na linha abaixo: ela monta sua chave ----
print("FLAG{" + str(kg_total) + "-" + str(valor_cha) + "}")
