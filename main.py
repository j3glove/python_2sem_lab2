import numpy as np
import random



def factorial(n):
    fact = 1
    for i in range(1 , 2*n):
        fact = fact*i
    return fact

def algorithm(n, X):
    det = np.linalg.det(np.linalg.matrix_power(X, (2 * n - 1)))
    result = det/factorial(n) * (-1)**n
    return result


try:
    while True:
        K=int(input("Введите размер матрицы от 3 до 50 "))
        if K >= 3 and K <= 50:
            break
        else:
            print("Ваше число не входит в данный диапазон")

    while True:
        t=int(input("Введите количество знаков после запятой от 1 до 20 включительно "))
        if t>=1 and t <= 20:
            break
        else:
            print("Ваше число не входит в данный диапазон")

    X = [[0] * K for i in range(K)]  # создание матрицы X
    for i in range(K):
        for j in range(K):
            X[i][j] = random.randint(-10, 10)

    #X = np.array([
    #    [7, -1, 3],
    #    [3, 1, -2],
    #    [3, 8, -5]
    #])

    summa = 0
    n=1
    while True:
        summa += algorithm(n,X)
        n+=1
        summastr = str(summa)
        if len(summastr) - summastr.find('.') >= t:
            print(summa)
            break

except:
    print("Произошла ошибка")