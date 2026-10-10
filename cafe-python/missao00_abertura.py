# =====================================================
#  CAFÉ PYTHON - Missão 0: Abrindo a loja
# =====================================================
# Você não precisa mudar nada neste arquivo. Só rode!
# No VS Code: clique no botão ▶ (canto superior direito)
# ou, no terminal, digite:  python missao00_abertura.py

import sys

print("Ligando o computador do Café & Letras...")

versao = sys.version_info
print("Python encontrado:", str(versao.major) + "." + str(versao.minor) + "." + str(versao.micro))

if versao.major < 3 or (versao.major == 3 and versao.minor < 10):
    print("ATENÇÃO: sua versão é antiga. Instale o Python 3.12 ou mais novo em python.org")

codigo = 0
for letra in "cafe-e-letras":
    codigo = codigo + ord(letra) * 7

print("Tudo pronto! Sua chave:")
print("FLAG{ABERTO-" + str(codigo) + "}")
