import sympy as sm
import numpy as np
import re


def parse_variables():
    '''
    Функция возвращает кориеж состоящий из переменных, которые являются sympy symbols
    :return:
    tuple of sympy symbols
    '''
    variables = ''
    flag_vars = False
    while not flag_vars:

        try:
            variables = input('Введите названия переменных, разделенных пробелом: ')
            if '(' in variables or ')' in variables:  # проверка на наличие не предусмотренных символов
                raise Exception
            if ',' in variables:
                variables = sm.parsing.sympy_parser.parse_expr(variables.replace(' ', ''))
                # при наличии ',', приведение к нужному формату убирая пробелы
            else:
                variables = sm.parsing.sympy_parser.parse_expr(variables.replace(' ', ','))
                # приведение к нужному формату
            flag_vars = True

        except Exception:
            print('Ошибка ввода. Введите две переменные через пробел, пример: x y')
    return variables


def parse_function(variables):
    '''
    Запускает парсер функции. Возвращает sympy expression
    :param variables: tuple of sympy symbols
    :return:
    sympy expression
    '''
    function = None
    flag_func = False
    while not flag_func:

        try:
            function = input('Введите функцию: ')
            function = sm.parsing.sympy_parser.parse_expr(function.replace('–', '-'))
            # заменяем минусы
#             check_var = function.free_symbols.difference(variables)
#             # проверяем не содержит ли функция лишние переменные
#             if len(check_var) != 0:
#                 print('Введены лишние переменные')
#                 raise Exception
            flag_func = True
        except Exception:
            print('Ошибка ввода. Введите функцию еще раз: ')
    return function


def parse_restriction(variables):
    '''
    Функция возвращает словарь, где ключом выступают названия переменных,
    значениями являются списки, с ограничивающими интервалами
    :param variables:
    :return: dict: key=variables, value=list
    '''
    restr_val = None
    flag_restriction = False
    while not flag_restriction:
        try:
            restrictions = input('Есть ли ограничения ? 1-да/ 0 – нет : ')
            if len(restrictions.strip()) == 1:
                restrictions = int(restrictions)
            else:
                raise Exception

            restr_val = {}
            if restrictions == 1:
                for var in variables:
                    restr_values = input(f'Введите ограничения по {str(var)}, если нет ограничений-введите 0:  -1 1 ')
                    restr_values = restr_values.strip()  # убираем пробелы в конце и начале
                    if restr_values == '0':
                        restr_val[var] = [-np.inf, np.inf]  # при отстутствии ограничений

                    else:
                        restr_values = restr_values.replace(',', ' ')  # проверка вводов
                        restr_values = re.sub(" +", " ", restr_values)  # убираем лишние пробелы

                        restr_val[var] = list(map(int, restr_values.split(' ')))
                        if len(restr_val[var]) != 2:
                            raise Exception
            elif restrictions == 0:
                for var in variables:
                    restr_val[var] = [-np.inf, np.inf]

            else:
                raise Exception

            flag_restriction = True
        except Exception:
            print('Ошибка ввода: ')
    return restr_val


def parse__restr_function(variables):
    '''
    Функция возвращает словарь, где ключом выступают названия переменных,
    значениями являются списки, с ограничивающими интервалами
    :param variables:
    :return: dict: key=variables, value=list
    '''
    restr_function = None
    flag_func = False
    while not flag_func:

        try:
            restr_function = input('Введите  огранеичивающую функцию: ')
            restr_function = sm.parsing.sympy_parser.parse_expr(restr_function.replace('–', '-'))
#             check_var = restr_function.free_symbols.difference(variables)
#             if len(check_var) != 0:
#                 print('Введены лишние переменные')
#                 raise Exception
            flag_func = True
        except Exception:
            print('Ошибка ввода. Введите функцию еще раз: ')
    return restr_function


def parser_task1():
    '''
    Функция почередно проверяющая все входные данные
    :return: tuple containing of: tuple, sympy expression, dict
    '''
    variables = parse_variables()
    func = parse_function(variables)
    restr = parse_restriction(variables)
    return variables, func, restr


def parser_task2():
    '''
    Функция почередно проверяющая все входные данные
    :return: tuple containing of: tuple, sympy expression, dict
    '''
    variables = parse_variables()
    func = parse_function(variables)
    restr = parse_restriction(variables)
    restr_func = parse__restr_function(variables)
    return variables, func, restr, restr_func
