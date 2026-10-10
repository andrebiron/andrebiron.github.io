# Café Python

Missões de Python para iniciantes. Você é o novo assistente de dados do Café & Letras, uma cafeteria com livraria.

## Como jogar

1. Crie uma pasta `cafe-python` no seu computador e baixe os arquivos abaixo para ela (clique com o botão direito no link e escolha "Salvar link como").
2. Abra a pasta no VS Code.
3. Em cada missão, leia os comentários dentro do arquivo e escreva o seu código no lugar indicado.
4. Rode o arquivo. Se estiver certo, ele mostra uma chave `FLAG{...}`.

## Missões

| Missão | Assunto | Arquivo |
|---|---|---|
| 0 | Rodar o primeiro programa | [missao00_abertura.py](missao00_abertura.py) |
| 1 | `print` e textos | Sem arquivo: veja abaixo |
| 2 | Variáveis e tipos | [missao02_estoque.py](missao02_estoque.py) |
| 3 | Contas e operadores | [missao03_playlist.py](missao03_playlist.py) |
| 4 | Trabalhando com textos | [missao04_bilhete.py](missao04_bilhete.py) |
| 5 | Decisões com `if` | Sem arquivo: veja abaixo |
| 6 | Listas e `for` | [missao06_vendas.py](missao06_vendas.py) |
| 7 | `while` e `break` | [missao07_enigmas.py](missao07_enigmas.py) |
| 8 | Desafio final: ler um arquivo | [missao08_desafio_final.py](missao08_desafio_final.py) e [vendas.csv](vendas.csv) |

Na missão 8, o `vendas.csv` precisa ficar na mesma pasta do `missao08_desafio_final.py`.

### Missão 1: o aviso do caixa

Crie o arquivo `aviso.py`, que mostra exatamente estas 5 linhas:

```
=== CAFÉ & LETRAS ===
Aberto das 7h às 20h
Café do dia: Bourbon Amarelo
Pão de queijo saindo agora!
=== BOM APETITE ===
```

### Missão 5: a regra do frete

Crie o arquivo `frete.py`, que pede o valor da compra com `input()` e mostra:

- `FRETE: R$ 15` se o valor for menor que 50
- `FRETE: R$ 8` se for de 50 até menos de 150
- `FRETE GRATIS` se for 150 ou mais

Dica: `valor = float(input("Valor da compra: "))`
