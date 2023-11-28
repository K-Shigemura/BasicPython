from math import sin, exp, pi, sqrt

def trapezoidal_integral(f, a = 0, b = 1, N = 100):
    h = (b - a) / N
    S=0
    for i in range(1, N):
        S += (f(a + i*h) + f(a + (i-1)+h)) * h / 2
        
    return S

print(trapezoidal_integral(sin, 0, pi/2, 50))
def f2(x):
    return 4/(x**2 + 1)
print(trapezoidal_integral(f2 , 0, 1, 100))
def f3(x):
    return sqrt(pi) * exp(-x**2)
print(trapezoidal_integral(f3, -100, 100, 1000))

# --example--
# print(sin(0))
# >>> 0
# -----------
