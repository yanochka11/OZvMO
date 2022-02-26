import OZvMO.parser as parser
import OZvMO.LocalExtrema as LocalExtrema
import OZvMO.plot as plot


def task1():
    variab, func, restr = parser.parser_task1()
    output_str, dots = LocalExtrema.local_extrema(variab, func, restr)
    fig = plot.plot(variab, func, restr, dots)

    return output_str, fig


