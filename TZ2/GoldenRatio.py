import pandas as pd
from typing import Literal


def golden_ratio(func, interval, pression=10 ** (-5), max_iter=500,
                 flag_results=False, flag_data=False, type_opt: Literal['min', 'max'] = 'min'):
    """
    Функция поиска экстремума функции одной переменной методом золотого сечения
    :param func: python function
    :param interval: list consisting of float numbers(left and right bounds)
    :param pression: optimization accuracy
    :param max_iter: maximum amount of iterations
    :param flag_results: flag: output of intermediate results
    :param flag_data: flag: recording intermediate results in a dataset
    :param type_opt: type of extrema: if min:flag_opt=1
                                      if max: flag_opt=-1

    :return: extrema:the point at which the extremum
             df: intermediate results in a dataset
    """
    if type_opt == 'min':
        flag_opt = 1
    else:
        flag_opt = -1
    data = []
    df = pd.DataFrame(columns=['iter', 'point', 'function'])
    phi = (5 ** 0.5 + 1) / 2
    a = interval[0]
    b = interval[1]
    extrema = (b + a) / 2

    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    if flag_data:
        data = [[0, extrema, func(extrema)]]
    if flag_results:
        print(f"Номер итерации {0}, точка {(a+b) / 2}, функция {func((a+b) / 2)}.")

    for i in range(max_iter):
        if abs(a - b) >= pression:
            if flag_opt * x1 > flag_opt * x2:
                a = x1
                x1 = b - (b - a) / phi
                x2 = a + (b - a) / phi
            else:
                b = x2
                x1 = b - (b - a) / phi
                x2 = a + (b - a) / phi
            extrema = (b + a) / 2

        else:
            break

        if flag_data:
            data.append(([i+1, extrema, func(extrema)]))
            df = pd.DataFrame(data, columns=['iter', 'point', 'function'])

        if flag_results:
            print(f"Номер итерации {i+1}, точка {extrema}, функция {func(extrema)}.")

    return extrema, df


if __name__ == '__main__':
    def f(x): return x ** 3 - x ** 2 - x


    print(golden_ratio(f, [0, 1.5], pression=10 ** (-5), max_iter=500,
                       flag_results=True, flag_data=False))
