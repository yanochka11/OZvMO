import numpy as np
from scipy.optimize import line_search


def bfgs(func,
         x0,
         c1 = 1e-4,
         c2 = 1e-1,
         max_func = 100,
         tolerance = 1e-8,
         max_iter = 500,
         flag_results=False, flag_data=False):
    xk = x0.copy()
    hk = np.eye((1, 1))
    for k in range(max_iter):
        grad_func = grad(func, xk)
        if norm2(grad_func) > tolerance:
            pk = -hk*grad(func, xk)
            alpha_k = line_search(func,
                                  lambda x: grad(func, xk).reshape(1, -1),
                                  c1=c1, c2=c2, maxiter=max_iter*10)[0]
            xk1 = xk + alpha_k * pk
            pass

        else:
            break
    else:
        pass


def grad(func, x0, delta_x = 1e-8):
    grad = []
    for i in range(len(x0)):
        delta_x_vec_plus = x0.copy()
        delta_x_vec_minus = x0.copy()
        delta_x_vec_plus[i] += delta_x
        delta_x_vec_minus[i] -= delta_x
        grad_i = (func(delta_x_vec_plus) - func(delta_x_vec_minus)) / (2 * delta_x)
        grad.append(grad_i)

    return grad

def norm2(vec):
    return sum(map(lambda x: x ** 2, vec)) ** 0.5

def calc_h_new(h, s, y):
    ro = 1 / (y.T @ s)
    i = np.eye(h.shape[0])
    h_new = (i - ro @ s @ y.T) @ h @ (i - ro @ s @ y.T) + ro @ s @ s.T
    return h_new