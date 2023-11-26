coefficients = [(1, -6, 9), (1, 2, -8), (8, -6, -35), (1, 0, 1)]

for a, b, c in coefficients:
    # TODO
    x1 = (-b+((b**2-4*a*c)**0.5))/(2*a)
    x2 = (-b-((b**2-4*a*c)**0.5))/(2*a)
    print(f"x={x1}, {x2} (a={a}, b={b}, c={c})")
