import OZvMO.parser as parser
import OZvMO.LocalExtrema as LocalExtrema
import OZvMO.plot as plot


def solve_task1():
    variab, func, restr = parser.parser_task1()
    sol_restr_all, sol_restr = LocalExtrema.local_extrema(variab, func, restr)
    fig = plot.plot(variab, func, restr, sol_restr)
    print(sol_restr_all)
    fig.show()


def solve_task2():
    variables, func, restr, restr_func = parser.parser_task2()
    sol_restr_all, sol_restr = LocalExtrema.lagrange(variables, func, restr, restr_func)
    fig = plot.plot(variables, func, restr, sol_restr)
    print(sol_restr_all)
    fig.show()
