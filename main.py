import numpy as np
import random



def factorial(n,oldfact):
    if oldfact !=1:
        fact = oldfact * (2*n - 1) * (2*n - 2)
    else:
        return 1
    return fact

def algorithm(n, X,oldfact):
    fact = 2 * n - 1
    currentfact = factorial(fact, oldfact)
    det = np.linalg.det(np.linalg.matrix_power(X, (2 * n - 1)))
    result = det/factorial(n, fact) * (-1)**n
    return result, currentfact


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

    rang = np.linalg.matrix_rank(X)

    #X = np.array([
    #    [7, -1, 3],
    #    [3, 1, -2],
    #    [3, 8, -5]
    #])

    summa = 0
    n=1
    summastr=""
    oldfact = 1
    tempsumma=0
    fraction = 0
    while True:
        tempsumma,oldfact=algorithm(n,X, oldfact)
        summa += tempsumma
        n+=1
        fraction = abs(summa) - abs(int(summa))
        print(n - 1, ' / ', summa)
        if fraction <= 10 ** (-t):
            print("Конечный результат:    , {1:.21f}".format(t, summa))
            break



except:
    print("Произошла ошибка")