# made in 2019 for my university python class as my final assignment, dubious clean coding

matp1 = [[3, 4, 2], [9, 1, 5], [6, 2, 4]]
matp2 = [[1, 7, 4], [2, 9, 3], [3, 6, 5]]


def matriz_pronta1(mat):
    print('Matriz Pronta 1:')
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'\033[34m[{mat[l][c]:^3.0f}]\033[m', end='')
        print()


def matriz_pronta2(mat):
    print('Matriz Pronta 2:')
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'\033[34m[{mat[l][c]:^3.0f}]\033[m', end='')
        print()


def make_zero_mat1():
    def zero_mat(l, c):
        matriz = []
        for a in range(l):
            matriz.append([])
            for b in range(c):
                matriz[a].append(0)
        print('Sua matriz é:')
        for a in range(len(matriz)):
            for b in range(len(matriz[a])):
                print(f'\033[34m[{matriz[a][b]:^3}]\033[m', end='')
            print()
        return matriz

    l = int(input('\033[33mLinhas: \033[m'))
    c = int(input('\033[33mColunas: \033[m'))

    zero_mat(l, c)


def zero_mat(l, c):
    matriz = []
    for a in range(l):
        matriz.append([])
        for b in range(c):
            matriz[a].append(0)
    print('Sua matriz é:')
    for a in range(len(matriz)):
        for b in range(len(matriz[a])):
            print(f'\033[34m[{matriz[a][b]:^3}]\033[m', end='')
        print()
    return matriz


def rand_mat1():
    def rand_mat(l, c):
        from random import randint
        matriz = []
        adder = []
        cont = 0
        while cont < 7:
            for a in range(0, l):
                for b in range(0, c):
                    x = randint(min, max)
                    adder.append(x)
                    cont += 1
                matriz.append(adder[:])
                adder.clear()
        print('Sua matriz é:')
        for a in range(0, l):
            for b in range(0, c):
                print(f'\033[34m[{matriz[a][b]:^4.0f}]\033[m', end='')
            print()
        return matriz

    linha = int(input('\033[33mLinhas: \033[m'))
    coluna = int(input('\033[33mColunas: \033[m'))
    min = int(input('\033[33mNumeros aleatórios entre: \033[m'))
    max = int(input('\033[33mE: \033[m'))

    rand_mat(linha, coluna)


def add_scalar(mat, n):
    for a in range(0, 3):
        for b in range(0, 3):
            mat[a][b] += n
    print(f'A Pronta1 + {n} é:')
    for a in range(0, 3):
        for b in range(0, 3):
            print(f'\033[34m[{mat[a][b]:^3.0f}]\033[m', end='')
        print()
    for a in range(0, 3):
        for b in range(0, 3):
            mat[a][b] -= n
    print()


def mul_scalar(mat, n):
    for a in range(0, 3):
        for b in range(0, 3):
            mat[a][b] *= n
    print(f'A Pronta1 x {n} é:')
    for a in range(0, 3):
        for b in range(0, 3):
            print(f'\033[34m[{mat[a][b]:^3.0f}]\033[m', end='')
        print()
    for a in range(0, 3):
        for b in range(0, 3):
            mat[a][b] /= n
    print()


def mat_min(mat):
    minmat = mat[0][0]
    for a in mat:
        for b in a:
            if b < minmat:
                minmat = b
    print(f'\033[33mO menor valor da Pronta1 é: {minmat}\033[m')


def mat_max(mat):
    matmax = mat[0][0]
    for a in mat:
        for b in a:
            if b > matmax:
                matmax = b
    print(f'\033[33mO maior valor de Pronta1 é: {matmax}\033[m')


def mat_mean(mat):
    cont = s = 0
    for a in mat:
        for b in a:
            s += b
            cont += 1
    x = float(s / cont)
    print(f'\033[33mO valor médio da Pronta1 é: {x}\033[m')


def diag(mat):
    matdig = []
    for a in range(len(mat)):
        for b in range(len(mat[a])):
            if a == b:
                matdig.append(mat[a][b])
    print('\033[33mOs números da diagonal são:')
    for g in matdig:
        print(f'{g:.0f} ', end='')
    print('\033[m')
    print()


def add(mat1, mat2):
    for a in range(len(mat1)):
        for b in range(len(mat1[a])):
            mat1[a][b] += mat2[a][b]
    print('Somando a Pronta1 e Pronta2 temos:')
    for a in range(len(mat1)):
        for b in range(len(mat1[a])):
            print(f'\033[34m[{mat1[a][b]:^3.0f}]\033[m', end='')
        print()
    for a in range(len(mat1)):
        for b in range(len(mat1[a])):
            mat1[a][b] -= mat2[a][b]
