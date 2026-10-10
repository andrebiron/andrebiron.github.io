# =====================================================
#  CAFÉ PYTHON - Missão 4: O bilhete da confeitaria
# =====================================================
# A confeiteira deixou um bilhete-charada sobre o horário de um bolo.
# (Textos entre parênteses em várias linhas viram UM texto só.)

bilhete = (
    "vez#gdoerkcagvt#ur# oza#hdd#ov zvoi#i#r#kjtrmampu#ubqqo mgso"
    "nags qii###uxakrs#o#l kge#pntcxagplr##sovlcnromuhdzcnd #dnmt"
    "#aomncqv# #qgaaqr#luurs#olcnjxe#vfckr yaeamdz#k qvodglj#yotq"
    "bcd ueoz"
)

# SUA MISSÃO: decifrar o bilhete, nesta ordem:
# 1. Remova todos os caracteres "#"                      (use .replace)
# 2. Pegue 1 caractere a cada 3, começando no índice 1   (fatiamento [inicio::passo])
# 3. Inverta o texto                                     (fatiamento [::-1])
# 4. Deixe tudo em MAIÚSCULAS                            (use .upper)
# 5. Troque os espaços por "_"                           (use .replace)
# Guarde o resultado final na variável resultado.

# ---- escreva seu código abaixo desta linha ----

resultado = ""

# ---- não mexa na linha abaixo ----
print("FLAG{" + resultado + "}")
