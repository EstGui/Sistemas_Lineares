from os import system

system('cls')

# G
def registrarMatriz():
    linha = int(input('Digite a quantidade de linhas: '))
    coluna = int(input('Digite a quantidade de colunas: '))

    matriz = [[]] * linha
    termoInd = []

    print('')
    for l in range(linha):
        for c in range(coluna):
            matriz[l].append(int(input(f'Digite o coeficiente da posição {l + 1} x {c + 1}: ')))
        termoInd.append(int(input(f'Digite o termo independente da linha {l + 1}: ')))
        print('')

    return matriz, termoInd

# D
def exibeMatriz(matriz, termoInd):
    xs = ['x'] * len(matriz)
    for c in range(len(xs)):
        xs[c] += str(c + 1)
        
    print(f'    {" ".join([str(x).center(6) for x in xs])}{"b".center(14)}')
    
    for c in range(len(matriz)):
        print(f'L{c + 1}| {" ".join([str(x).center(6) for x in matriz[c]])}  ={str(termoInd[c]).center(8)}')

# G
def exibeResultado(resultado):
    print('Resultado\n'.center(34))
    for i, v in enumerate(resultado):
        print(f'X{i + 1} = {v}')

    print('='*34)


def gauss(matriz, b):
    nl = len(matriz)
    nc = len(matriz[0])
    
    # D
    for i in range(nl - 1):
        for j in range(i + 1, nl):
            fator_multiplicador = matriz[j][i] / matriz[i][i]
            for c in range(nc):
                matriz[j][c] -= fator_multiplicador * matriz[i][c]
            b[j] -= fator_multiplicador * b[i]
    
    # G
    resultado = [0] * nc
    for i in range(nl - 1, -1, -1):
        resultado[i] = b[i] / matriz[i][i]
        for j in range(i + 1, nl):
            resultado[i] -= matriz[i][j] * resultado[j] / matriz[i][i]

    return resultado


def continuar():
    continua = input("\nDeseja resolver um novo sistema? [S/N]: ").upper().strip()

    while continua not in 'SN':
        system('cls')
        print("Opção inválida, digite novamente")
        continua = input("Deseja resolver um novo sistema? [S/N]: ").strip().upper()

    return True if continua == 'S' else False


def main():
    opt = None
    exe = True
    while opt != 0 and exe:
        print('='*34)
        print('Sistemas Lineares'.center(34))
        print('='*34)

        opt = int(input("""[1] Resolver Sistema
                        
[0] Encerrar o programa
----------------------------------
Selecione a opção desejada: """))
        
        if opt == 1:
            system('cls')
            matriz, termoInd = registrarMatriz()
            
            system('cls')
            print('='*34)
            print('Matriz Original\n'.center(34))
            exibeMatriz(matriz, termoInd)
            
            resultado = gauss(matriz, termoInd)

            print('='*34)
            print('Matriz Escalonada\n'.center(34))
            exibeMatriz(matriz, termoInd)
            print('='*34)

            exibeResultado(resultado)

            exe = continuar()

        elif not opt:
            break

    system('cls')
    print("\nFinalizando Programa...")


main()
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
