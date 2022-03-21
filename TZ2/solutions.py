from OZvMO.TZ2.ParserTZ2 import parser_task_gr
from OZvMO.TZ2.GoldenRatio import golden_ratio
from OZvMO.TZ2.parabols import parabolic_interpolation
from IPython.display import display


def solve_golden_ratio(precision=1e-5, max_iter=500,
                       flag_results=False, flag_data=False, type_opt='min'):
    """
    Функция поиска экстремума функции одной переменной методом золотого сечения
    :param precision: optimization accuracy
    :param max_iter: maximum amount of iterations
    :param flag_results: output of intermediate results
    :param flag_data: recording intermediate results in a dataset
    :param type_opt: type of extrema: if min:flag_opt=1
                                      if max: flag_opt=-1
    :return:
    """
    variables, func, interval = parser_task_gr()

    func, interval, extrema, df = golden_ratio(func, interval, pression=precision, max_iter=max_iter,
                                               flag_results=flag_results, flag_data=flag_data, type_opt=type_opt)
    if df.shape[0] != 0:
        display(df)
    print(f'точка экстремума: x = {extrema}, значение функции {func(extrema)}.')
    return func, interval, df

def solve_parabolic_interpolation(precision=1e-5, max_iter=500,
                                  flag_results=False, flag_data=False, type_opt='min'):
    """
    Функция поиска экстремума функции одной переменной методом парабол
    :param precision: optimization accuracy
    :param max_iter: maximum amount of iterations
    :param flag_results: output of intermediate results
    :param flag_data: recording intermediate results in a dataset
    :param type_opt: type of extrema: if min:flag_opt=1
                                      if max: flag_opt=-1
    :return:
    """
    variables, func, interval = parser_task_gr()

    extrema, df = parabolic_interpolation(func, interval, pression=precision, max_iter=max_iter,
                                          flag_results=flag_results, flag_data=flag_data, type_opt=type_opt)
    if df.shape[0] != 0:
        display(df)
    print(f'точка экстремума: x = {extrema}, значение функции {func(extrema)}.')


def solve_brent(pression=1e-5, max_iter=500,
                flag_results=False, flag_data=False, type_opt='min'):
    """
    Функция поиска экстремума функции одной переменной методом Брента
    :param pression: optimization accuracy
    :param max_iter: maximum amount of iterations
    :param flag_results: output of intermediate results
    :param flag_data: recording intermediate results in a dataset
    :param type_opt: type of extrema: if min:flag_opt=1
                                      if max: flag_opt=-1
    :return:
    """
    variables, func, interval = parser_task_gr()

    extrema, df = parabolic_interpolation(func, interval, pression=pression, max_iter=max_iter,
                                          flag_results=flag_results, flag_data=flag_data, type_opt=type_opt)
    if df.shape[0] != 0:
        display(df)
    print(f'точка экстремума: x = {extrema}, значение функции {func(extrema)}.')


if __name__ == '__main__':
    solve_parabolic_interpolation(precision=1e-5, max_iter=500,
                                  flag_results=True, flag_data=True, type_opt='min')
