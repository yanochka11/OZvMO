from parser import parser_task1
from LocalExtrema import local_extrema
from plot import plot


def task1():
    variab, func, restr = parser_task1()
    output_str, dots = local_extrema(variab, func, restr)
    fig = plot(variab, func, restr, dots)

    return output_str, fig