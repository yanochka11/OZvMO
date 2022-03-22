from typing import Callable, Any, Tuple, Dict, TypedDict, List, Sequence
from numbers import Real
import numpy as np
from scipy.optimize import line_search


def bfgs(function: Callable[[Sequence[Real], Any], Real],
         x0: List[Real],
         c1: Real = 1e-4,
         c2: Real = 1e-1,
         max_func: Real = 100,
         tolerance: Real = 1e-8,
         max_iter: Real = 500,
         verbose: bool = False,
         keep_history: bool = False) -> Tuple[Dict, TypedDict]:
    """
    BFGS method
    :param function:
    :param x0:
    :param c1:
    :param c2:
    :param max_func:
    :param tolerance:
    :param max_iter:
    :param verbose:
    :param keep_history:
    :return:
    """
    xk = x0.copy()
    hk = np.eye((1,1))
    for k in range(max_iter):
        grad_func = gradient(function, xk)
        if norm2(grad_func) > tolerance:
            pk = -hk*gradient(function, xk)
            alpha_k = line_search(function,
                                  lambda x: gradient(function, x, **kwargs).reshape(1, -1),
                                  c1=c1 c2=c2, maxiter=max_iter*10)[0]
            xk1 =
            pass

        else:
            break
    else:
        pass


def gradient(function: Callable[[Sequence[Real], Any], Real],
             x0: List[Real],
             delta_x = 1e-8) -> Sequence[Real]:
    """
    Calculate gradient
    :param function:
    :param x0:
    :return:
    """
    grad = []
    for i in range(len(x0)):
        delta_x_vec_plus = x0.copy()
        delta_x_vec_minus = x0.copy()
        delta_x_vec_plus[i] += delta_x
        delta_x_vec_minus[i] -= delta_x
        grad_i = (function(delta_x_vec_plus) - function(delta_x_vec_minus)) / (2 * delta_x)
        grad.append(grad_i)

    return grad


def norm2(vec: Sequence[Real]) -> Real:
    """
    Return l2 norm
    :param vec:
    :return:
    """
    return sum(map(lambda x: x ** 2, vec)) ** 0.5

def calc_h_new(h: np.ndarray,
               s: np.ndarray,
               y: np.ndarray) -> np.ndarray:
    """
    Calculate new H_k+1 matrix
    :param h:
    :param s:
    :param y:
    :return:
    """
    ro = 1 / (y.T @ s)
    i = np.eye(h.shape[0])
    h_new = (i - ro @ s @ y.T) @ h @ (i - ro @ s @ y.T) + ro @ s @ s.T


if __name__ == '__main__':
    def func(x): return x[0] ** 2 + x[1] ** 2
    print(gradient(func, [1, 1]))

