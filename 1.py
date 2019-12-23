from sympy import *


def calc(start, now, years):
    q = Symbol('q')
    x = abs(N(solve(start * (q ** years) - now)[0]))
    return x - 1


print(calc(15, 47, 7))
