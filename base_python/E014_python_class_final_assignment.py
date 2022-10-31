# made in 2019 for my university python class as my final assignment, dubious clean coding

import E015_python_class_final_assignment_math as mat
from time import sleep

print('''\033[31m
[1] matriz com zeros.
[2] matriz com números aleatórios.\033[m''')

escolha = int(input('\033[32mComo será sua matriz? \033[m'))
sleep(1)
print()

if escolha == 1:
    suamatriz = mat.make_zero_mat1()

if escolha == 2:
    suamatriz = mat.rand_mat1()

print()

print('Decidi colocar duas matrizes minhas.')
sleep(1)
mat.matriz_pronta1(mat.matp1)
print()
sleep(1)
mat.matriz_pronta2(mat.matp2)

print()

n = int(input('\033[36mEscolha um escalar: \033[m'))
sleep(1)
mat.add_scalar(mat.matp1, n)
sleep(1)
mat.mul_scalar(mat.matp1, n)
sleep(1)
mat.mat_min(mat.matp1)
sleep(1)
mat.mat_max(mat.matp1)
sleep(1)
mat.mat_mean(mat.matp1)
sleep(1)
mat.diag(mat.matp1)
sleep(1)
mat.add(mat.matp1, mat.matp2)
print()
sleep(1)
print('\033[Thanks for reading!')
