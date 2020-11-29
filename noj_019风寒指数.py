def windchill(v, t):
    # windchill = 13.12 + 0.6215t - 11.37v^0.16 + 0.3965t*v^0.16
    wc = 13.12 + 0.6215*t - 11.37*v**0.16 + 0.3965*t*v**0.16
    print(round(wc))

v = float(input())
t = float(input())
windchill(v, t)