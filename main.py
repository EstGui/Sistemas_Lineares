# # 3x + 2y - z = 5
# # 3x + 2y - z = 5
# # 3x1 + 2x2 - x3 = 5


# def mostrarMatriz(matriz, ):
#     pass

# #Criação do Sistema Linear
# linha = int(input('Digite a quantidade de linhas: '))
# coluna = int(input('Digite a quantidade de colunas: '))

# matriz = []
# termoInd = []

# for c in range(linha):
#     matriz.append([])

# for l in range(linha):
#     for c in range(coluna):
#         matriz[l].append(int(input(f'Digite o coeficiente da posição {l + 1} x {c + 1}: ')))
#     termoInd.append(int(input(f'Digite o termo independente da linha {l + 1}: ')))


# for c in range(len(matriz)):
#     print(f'{matriz[c]} = {termoInd[c]}')


# """
# METODO DE GAUSS

# Calculo Do Fator Multiplicador

# FM = Fator Multiplicador
# P = Pivo
# NT0 = Number To 0

# ======== FM = NT0/P ========


# Calculo Para Zerar Os Valores Do Sistema

# ======== 0 = NT0 - FM * P ========

# IMPORTANTE LEMBRAR QUE: 
#     - A primeira linha do sistema nao tem numeros para zerar
#     - O pivo mudara de acordo com a linha e coluna do numero a ser zerado
#     - O numeros a serem zerados por linhar seram sempre os primeiros e a quantidade deles sera sempre o numero da linha - 1 (Linha 3 - 1 = 2 numeros a serem zerados)

# """
      

def gauss(matriz, b, nl, nc):
    for l in range(l + 1, nl):
        for c in range(nc):
            fator -= matriz[l][c] / matriz[l][l]
            for f in range(c, nc):
                matriz[l][f] -= fator * matriz[l][f]
            b[l] -= fator * b[c]


# ------------------------------------------------------------------------
def gauss_gpt(matriz, b):
    n = len(matriz)

    for i in range(n):
        for j in range(i+1, n): 
            fator_multiplicador = matriz[j][i] / matriz[i][i]
            for k in range(i, n):
                matriz[j][k] -= fator_multiplicador * matriz[i][k]
            b[j] -= fator_multiplicador * b[i]

    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i] / matriz[i][i]
        for j in range(i+1, n):
            x[i] -= matriz[i][j] * x[j] / matriz[i][i]

    return x
# ------------------------------------------------------------------------

def gauss_2(matriz, b, nl, nc):
    fator_multiplicador = matriz[1][0] / matriz[0][0]
    matriz[1] = [x * fator_multiplicador for x in matriz[1]]


# A = [[4, 3, -2],
#      [1, 1, 2],
#      [3, 2, 4]]

# b = [3, 2, 1]

# Fm21 = 1/4 = 21/11 = 0,25

# Coeficientes do sistema (matriz A)
A = [
    [4, -2, 3],
    [1, 5, -1]
]

# Resultados do sistema (vetor b)
b = [10, -3]

solucao = gauss(A, b)
print("A solução do sistema é:", solucao)




def gauss_jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(A)
    x = x0[:]
    x_new = [0] * n

    for _ in range(max_iter):
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]

        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new

        x = x_new[:]

    raise ValueError("O método de Gauss-Jacobi não convergiu dentro do número máximo de iterações.")

A = [
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
]
b = [7, -8, 6]

x0 = [0, 0, 0]

solution = gauss_jacobi(A, b, x0)

# print("A solução do sistema é:", solution)
