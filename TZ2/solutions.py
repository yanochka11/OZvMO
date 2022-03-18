import OZvMO.TZ2.ParserTZ2 as parser
import OZvMO.TZ2.GoldenRatio as GoldenRatio
from IPython.display import display

def solve_golden_ratio():
    variables, func, interval = parser.parser_task_gr()
    extrema, df = golden_ratio(func, interval, pression=10 ** (-5), max_iter=500,
                 flag_results=False, flag_data=False, type_opt: Literal['min', 'max'] = 'min')
    if df.shape[0] != 0:
        display(df)
    print(f'точка экстремума: x = {extrema}')