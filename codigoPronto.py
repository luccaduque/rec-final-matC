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
uniao = set()

for u in usuarios_anuncio_A:
    uniao.add(u)

for u in usuarios_anuncio_B:
    uniao.add(u)

    
intersecao = usuarios_anuncio_A & usuarios_anuncio_B
diferenca_A_B = usuarios_anuncio_A - usuarios_anuncio_B
diferenca_B_A = usuarios_anuncio_B - usuarios_anuncio_A

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
i = 2
while i <= 7:
    pa_valores.append(pa_inicial + (i - 1) * pa_razao)
    i = i + 1



# TODO: calcule os próximos 5 termos da PG (Dia 2 ao Dia 6)
pg_valores = []  # substitua pela lista correta
i = 2
while i <= 6:
    pg_valores.append(pg_inicial * (pg_razao ** (i - 1)))
    i = i + 1


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
custo_total = a * usuarios_ativos + b 

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
delta = (b_q ** 2) - (4 * a_q * c_q)  # substitua

# TODO: calcule as raízes x1 e x2 (use apenas operadores básicos e **0.5 para raiz)
sqrt_delta = delta ** 0.5
x1 = (-b_q + sqrt_delta) / (2 * a_q)  
x2 = (-b_q - sqrt_delta) / (2 * a_q)
# TODO: calcule o vértice: Xv = -b/(2a), Yv = valor de y em Xv
xv = -b_q / (2 * a_q)  # substitua
yv = a_q * (xv ** 2) + b_q * xv + c_q  # substitua

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
matriz_transposta = []  
j = 0

while j < len(matriz_features[0]):
    linha_t = []
    i = 0
    while i < len(matriz_features):
        linha_t.append(matriz_features[i][j])
        i += 1
    matriz_transposta.append(linha_t)
    j += 1

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
determinante = (1*0*6 + 4*5*3 + 3*2*2) - (3*0*3 + 1*5*2 + 4*2*6)

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
destinos_home = mapa_app['Home']   # substitua
destinos_perfil = mapa_app['Perfil'] # substitua

print("A partir de 'Home' o usuário pode ir para:", destinos_home)
print("A partir de 'Perfil' o usuário pode ir para:", destinos_perfil)
print()

# =========================================================
# Item 8 – Estatística: Tempo de Uso (20 pontos)
# =========================================================

print("=== Item 8: Estatística – Tempo de Uso ===")

tempos_uso = [15, 10, 22, 18, 10, 12, 40, 30, 8, 15]

# TODO: calcule a média
soma = 0
i = 0
while i < len(tempos_uso):
    soma = soma + tempos_uso[i]
    i = i + 1
media = soma / len(tempos_uso)

# TODO: calcule a mediana (lista precisa estar ordenada)
ordenados = sorted(tempos_uso)
n = len(ordenados)

if n % 2 == 0:
    mediana = (ordenados[n//2 - 1] + ordenados[n//2]) / 2
else:
    mediana = ordenados[n//2]

# TODO: calcule a(s) moda(s)
modas = []
frequencias = {}

i = 0
while i < len(tempos_uso):
    valor = tempos_uso[i]
    if valor in frequencias:
        frequencias[valor] = frequencias[valor] + 1
    else:
        frequencias[valor] = 1
    i = i + 1

maior_frequencia = 0
for v in frequencias:
    if frequencias[v] > maior_frequencia:
        maior_frequencia = frequencias[v]

for v in frequencias:
    if frequencias[v] == maior_frequencia and maior_frequencia > 1:
        modas.append(v)

# TODO: calcule a variância (média dos quadrados dos desvios)
soma_quadrados = 0
i = 0
while i < len(tempos_uso):
    diferenca = tempos_uso[i] - media
    soma_quadrados = soma_quadrados + (diferenca ** 2)
    i = i + 1

variancia = soma_quadrados / len(tempos_uso)

# TODO: calcule o desvio padrão (raiz quadrada da variância)
desvio_padrao = variancia ** 0.5

print("Média:", media)
print("Mediana:", mediana)
print("Moda(s):", modas)
print("Variância:", variancia)
print("Desvio padrão:", desvio_padrao)
print()

print("=== Fim do Desafio ===")