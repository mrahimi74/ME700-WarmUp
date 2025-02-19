def Avg(x, y):
    return (x + y) / 2

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def abs(x):
    if x >= 0:
        return x
    else:
        return -x

def check(a: float, b: float):
    if a >= b:
        raise ValueError("a must be smaller than b")
    return True


def opps_sign(a, b, func):
    if func(b) * func(a) < 0:
        return True
    else:
        raise ValueError("function should have opposite signs")

def bisection(a, b, max_iter, tol, func):
    iter = 1
    c_history = []
    if opps_sign(a, b, func):
        c = Avg(a, b)
        c_history.append(c)
        while abs(c - a) > tol or func(c) > tol:
            if sign(func(c)) == sign(func(a)):
                a = c
            else:
                b = c

            c = Avg(a, b)
            c_history.append(c)
            iter += 1
            if max_iter < iter:
                raise ValueError("Solution did not converge as the maximum iteration reached")
                break
        else:
            return c, c_history, iter