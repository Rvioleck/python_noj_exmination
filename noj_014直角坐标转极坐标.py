import math
def cartesian2polar(a, b):
    c = (a**2 + b**2)**0.5
    theta = math.atan(b/a)
    print("{:.4f},{:.4f}".format(c, theta))

a = float(input())
b = float(input())
cartesian2polar(a, b)