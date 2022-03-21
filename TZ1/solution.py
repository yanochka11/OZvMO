import OZvMO.parser as parser
import OZvMO.LocalExtrema as LocalExtrema
import OZvMO.plot as plot
from IPython.display import display

def solve_task1():
    variab, func, restr = parser.parser_task1()
    try:
        sol_restr_all, sol_restr = LocalExtrema.local_extrema(variab, func, restr)
    except Exception:
        print('Решений не находится')
        sol_restr = []
        sol_restr_all = []
    if len(sol_restr_all) == 0:
        
         sol_restr_all = 'нет точек экстремума'
    fig = plot.plot(variab, func, restr, sol_restr)
    display(sol_restr_all)
    fig.show()


def solve_task2():
    variables, func, restr, restr_func = parser.parser_task2()
    try:
        sol_restr_all, sol_restr = LocalExtrema.lagrange(variables, func, restr, restr_func)
    except Exception:
        print('Решений не находится')
        sol_restr = [] 
        sol_restr_all = []
    if len(sol_restr_all) == 0:
         sol_restr_all = 'нет точек экстремума'
    fig = plot.plot(variables, func, restr, sol_restr)
    display(sol_restr_all)
    fig.show()
