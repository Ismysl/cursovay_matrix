"""
Программа cursovay
Курсовой проект
по предмету МДК 01.01 Разработка программных модулей
по теме: «Обращение квадратных матриц»
Язык программирования Python
Разработал: Мыслицкий И. М.
Задание: Разработка программы обращение 
квадратных матриц методом Гаусса

Переменные, используемые в программе:
m – хранит «склеенную» матрицу;
matrix_origin – хранит начальную матрицу;
n – хранит размер матрицы;
dt – хранит значения детерминанта матрицы;
I – хранит значение искомой обратной матрицы;
A – хранит обратную матрицы от полученной;
swap_row – хранит индекс первой строки;
m1 – хранит преобразованную матрицу;
m_str – хранит матрицу в формате строки.

"""

#подключение библиотек
import numpy as np
import sys

def inverse(matrix_origin, flag):
    m = np.hstack((matrix_origin, np.matrix(np.diag([1.0 for i in range(matrix_origin.shape[0])]))))
    if flag == True:
        print_matrix(m)

    # прямой ход
    for k in range(n):
        # 1) Поменять местами k-ряд с одним из базовых, если m[k, k] = 0
        swap_row = pick_nonzero_row(m, k)
        if swap_row != k:
            m[k, :], m[swap_row, :] = m[swap_row, :], np.copy(m[k, :])
        # 2) Сделать диагональный элемент равным 1
        if m[k, k] != 1:
            m[k, :] *= 1 / m[k, k]
        if flag == True:
            print_matrix(m)
        # 3) Сделать все базовые элементы в столбце равными нулю
        for row in range(k + 1, n):
            m[row, :] -= m[k, :] * m[row, k]
        if flag == True:
            print_matrix(m)

    # обратный ход
    for k in range(n - 1, 0, -1):
        for row in range(k - 1, -1, -1):
            if m[row, k]:
                # 1) Сделать все вышележащие элементы равными нулю в единичной матрице
                m[row, :] -= m[k, :] * m[row, k]
        if flag == True:
            print_matrix(m)
    return np.hsplit(m, 2)[1]

def pick_nonzero_row(m, k):
    while k < m.shape[0] and not m[k, k]:
        k += 1
    return k

# вывод решения
def print_matrix(m):
    m1 = np.array(m, dtype=float)

    for i in range(n):
        for j in range(n * 2):
            m1[i][j] = round(m1[i][j], 5)

    m_str = '\n'.join([''.join(['{:10}'.format(item) for item in row]) for row in m1])
    print(m_str)
    print('─' * 100)


m1 = []
n = 0
while (n < 2) or (n > 5):
    try:
        n=int(input("Введите размерность матрицы (больше 1 или меньше 6): "))
        if (n < 2) or (n > 5):
            print('Введите другую размерность матрицы')
    except ValueError:
        print("Это не число.")

# инициализировать матрицу nxn нулями
matrix_origin=np.zeros((n,n))

# ввод матрицы
for i in range(n):
    for j in range(n):
        try:
            matrix_origin[i][j]=int(input())
        except ValueError:
            print("Это не число. Введите элемент снова ")
	matrix_origin[i][j]=int(input())
print("Начальная матрица: ")
print(matrix_origin)
print("Решение: ")

# проверка на детерминант
dt = np.linalg.det(matrix_origin)
if dt == 0:
    print("Детерминант равен 0. Невозможно найти обратную матрицу")
    sys.exit()


I = inverse(matrix_origin, True)
print("Ответ: ")
print('Обратная матрица ')
print(I)
print('─' * 100)
print("Проверка: ")
print('Обратная от полученой матрицы (исходная) ')
A = inverse(I, False)
print(A)

if round(np.linalg.det(I), 4) == round(1 / np.linalg.det(matrix_origin), 4):
    print("Детерминант исходной матрицы равен детерминанту обратной матрицы")