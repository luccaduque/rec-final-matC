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
x1 = (-b_q + sqrt_delta) / (2 * a_q)  # substitua
x2 = (-b_q - sqrt_delta) / (2 * a_q)  # substitua

# TODO: calcule o vértice: Xv = -b/(2a), Yv = valor de y em Xv
xv = -b_q / (2 * a_q)  # substitua
yv = a_q * (xv ** 2) + b_q * xv + c_q  # substitua

print("Delta:", delta)
print("Raiz x1:", x1)
print("Raiz x2:", x2)
print("Vértice (Xv, Yv):", xv, yv)
print()