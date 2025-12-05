# Desafio – Análise de Dados com Python Básico
# ATENÇÃO:
# - Não usar import (nenhuma biblioteca).
# - Não usar def (nenhuma função definida pelo usuário).
# - Código totalmente procedural.

print("=== Desafio – Análise de Dados com Python Básico ===")
print()

# =========================================================
# Item 1 – Conjuntos: Quem Viu o Quê? (10 pontos)
# =========================================================

print("=== Item 1: Conjuntos – Quem Viu o Quê? ===")

usuarios_anuncio_A = {101, 102, 103, 104, 105}
usuarios_anuncio_B = {104, 105, 106, 107}

# TODO: calcule os conjuntos pedidos
uniao = set()           # substitua pelo cálculo correto
intersecao = set()      # substitua
diferenca_A_B = set()   # substitua
diferenca_B_A = set()   # substitua

print("Uniao:", uniao)
print("Intersecao:", intersecao)
print("Diferenca A - B:", diferenca_A_B)
print("Diferenca B - A:", diferenca_B_A)
print()

# =========================================================
# Item 2 – Sequências: Crescimento de Usuários (10 pontos)
# =========================================================

print("=== Item 2: Sequências – Crescimento de Usuários ===")

# PA: começa com 120 e cresce +15 por dia
pa_inicial = 120
pa_razao = 15

# PG: começa com 40 e cresce 50% por dia (razão 1.5)
pg_inicial = 40
pg_razao = 1.5

# TODO: calcule os próximos 6 termos da PA (Dia 2 ao Dia 7)
pa_valores = []  # substitua pela lista correta

# TODO: calcule os próximos 5 termos da PG (Dia 2 ao Dia 6)
pg_valores = []  # substitua pela lista correta

print("PA - próximos 6 dias:", pa_valores)
print("PG - próximos 5 dias:", pg_valores)
print()

# =========================================================
# Item 3 – Função Afim: Custo do Servidor (10 pontos)
# =========================================================

print("=== Item 3: Função Afim – Custo do Servidor ===")

a = 0.25  # custo por usuário ativo
b = 50.0  # custo fixo diário
usuarios_ativos = 1500

# TODO: calcule o custo total y = a*x + b
custo_total = 0.0  # substitua pelo cálculo correto

print("Custo total para", usuarios_ativos, "usuarios ativos:", custo_total)
print()

# =========================================================
# Item 4 – Função Quadrática: Engajamento (15 pontos)
# =========================================================

print("=== Item 4: Função Quadrática – Engajamento ===")

# y = -2x^2 + 20x
a_q = -2
b_q = 20
c_q = 0

# TODO: calcule o Delta = b^2 - 4ac
delta = 0  # substitua

# TODO: calcule as raízes x1 e x2 (use apenas operadores básicos e **0.5 para raiz)
x1 = 0.0  # substitua
x2 = 0.0  # substitua

# TODO: calcule o vértice: Xv = -b/(2a), Yv = valor de y em Xv
xv = 0.0  # substitua
yv = 0.0  # substitua

print("Delta:", delta)
print("Raiz x1:", x1)
print("Raiz x2:", x2)
print("Vértice (Xv, Yv):", xv, yv)
print()

# =========================================================
# Item 5 – Matrizes: Análise de Features (15 pontos)
# =========================================================

print("=== Item 5: Matrizes – Análise de Features ===")

matriz_features = [
    [10, 15, 5],  # Usuário 1
    [5, 20, 7],   # Usuário 2
    [12, 10, 3]   # Usuário 3
]

# TODO: calcule a matriz transposta (3x3)
# Dica: linha vira coluna e coluna vira linha.
matriz_transposta = []  # substitua pela matriz transposta

print("Matriz transposta:")
print(matriz_transposta)
print()

# =========================================================
# Item 6 – Determinante 3x3: Chave de Segurança (10 pontos)
# =========================================================

print("=== Item 6: Determinante 3x3 – Chave de Segurança ===")

matriz_seguranca = [
    [1, 4, 3],
    [2, 0, 5],
    [3, 2, 6]
]

# TODO: calcule o determinante usando a Regra de Sarrus
determinante = 0  # substitua pelo cálculo correto

print("Determinante da matriz de segurança:", determinante)
print()

# =========================================================
# Item 7 – Grafos: Navegação do Usuário (10 pontos)
# =========================================================

print("=== Item 7: Grafos – Navegação do Usuário ===")

mapa_app = {
    'Login': ['Home'],
    'Home': ['Feed', 'Perfil', 'Login'],
    'Perfil': ['Home', 'Config'],
    'Feed': ['Home'],
    'Config': ['Perfil']
}

# TODO: obtenha a lista de destinos a partir de 'Home' e 'Perfil'
destinos_home = []   # substitua
destinos_perfil = [] # substitua

print("A partir de 'Home' o usuário pode ir para:", destinos_home)
print("A partir de 'Perfil' o usuário pode ir para:", destinos_perfil)
print()

# =========================================================
# Item 8 – Estatística: Tempo de Uso (20 pontos)
# =========================================================

print("=== Item 8: Estatística – Tempo de Uso ===")

tempos_uso = [15, 10, 22, 18, 10, 12, 40, 30, 8, 15]

# TODO: calcule a média
media = 0.0  # substitua

# TODO: calcule a mediana (lista precisa estar ordenada)
mediana = 0.0  # substitua

# TODO: calcule a(s) moda(s)
modas = []  # substitua por lista com o(s) valor(es) modal(is)

# TODO: calcule a variância (média dos quadrados dos desvios)
variancia = 0.0  # substitua

# TODO: calcule o desvio padrão (raiz quadrada da variância)
desvio_padrao = 0.0  # substitua

print("Média:", media)
print("Mediana:", mediana)
print("Moda(s):", modas)
print("Variância:", variancia)
print("Desvio padrão:", desvio_padrao)
print()

print("=== Fim do Desafio ===")
