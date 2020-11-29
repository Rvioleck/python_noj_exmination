import math

def rgb2hsv(r, g, b):
    v = max0 = max(r, g, b)
    min0 = min(r, g, b)
    if v != 0:
        s = (max0-min0)/max0
    else:
        s = 0
    if max0 == r:
        h = (g-b)/(max0-min0)
    elif max0 == g:
        h = 2 + (b-r)/(max0-min0)
    elif max0 == b:
        h = 4 + (r-g)/(max0-min0)
    h *= 60
    if h < 0:
        h += 360
    v /= 255
    print("{:.4f},{:.4%},{:.4%}".format(h, s, v))

r = int(input())
g = int(input())
b = int(input())
rgb2hsv(r, g, b)