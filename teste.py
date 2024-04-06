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

def gauss_2(matriz, b):
    n = len(matriz)
    nc = len(matriz[0])

    for k in range(n-1):
        for j in range(k+1, n):
            fator_multiplicador = matriz[j][k] / matriz[k][k]
            for c in range(nc):
                matriz[j][c] -= fator_multiplicador * matriz[k][c]
            b[j] -= fator_multiplicador * b[k]


    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i] / matriz[i][i]
        for j in range(i+1, n):
            x[i] -= matriz[i][j] * x[j] / matriz[i][i]

    # return x

    # for c in range():
    # fator_multiplicador = matriz[1][0] / matriz[0][0]
    # for c in range(nc):
    #     matriz[1][c] -= fator_multiplicador * matriz[0][c]
    # b[1] -= fator_multiplicador * b[0]


    # fator_multiplicador = matriz[2][0] / matriz[0][0]
    # for c in range(nc):
    #     matriz[2][c] -= fator_multiplicador * matriz[0][c]
    # b[2] -= fator_multiplicador * b[0]


    # fator_multiplicador = matriz[2][1] / matriz[1][1]
    # for c in range(nc):
    #     matriz[2][c] -= fator_multiplicador * matriz[1][c]
    # b[2] -= fator_multiplicador * b[1]

    # print(fator_multiplicador)
    # print(matriz[1])
    # print(b[1])



A = [[4, 3, -2],
     [1, 1, 2],
     [3, 2, 4]]

b = [3, 2, 1]


# A = [[2, 3, -1],
#      [4, -1, 2]]

# b = [5, 7]

# Fm21 = 1/4 = 21/11 = 0,25

solucao = gauss_2(A, b)
print("A solução do sistema é:", solucao)