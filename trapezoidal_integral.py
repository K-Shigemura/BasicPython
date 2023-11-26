from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------
N = 100
a = 0
b =  pi/2

S = 0
h = (b - a) / N
for i in range(N):
    S += (sin(a + i * h) + sin(a + (i + 1))) * h / 2

print(S)
