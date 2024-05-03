from decimal import *

getcontext().prec = 149
getcontext().rounding = ROUND_HALF_UP
D = Decimal
pi = D('3.1415926535897932384626433832795028841971693993751058209749')

def sin(x):
    x %= D(2 * pi)
    n = D(1)
    k, cur = D(0), D(x)
    res = D(x)
    sign = D(-1)
    while (abs(cur) >= 10 ** (-60)):
        n += 2
        fac = D(n * (n - 1))
        cur = (cur * x * x) / fac * sign
        res += cur
    return res

def f(x):
    return a * x + b * sin(x) - c

a, b, c = map(int, input().split())
l, r = D(0), D(10 ** 6)
x = (l + r) / 2

while (abs(r - l) >= 10 ** (-60)):
    if (f(x) > 0): r = x
    else: l = x
    x = (l + r) / 2

print(round(x, 6))