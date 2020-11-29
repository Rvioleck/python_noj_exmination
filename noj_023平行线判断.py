def slope(x1, y1, x2, y2):
    # 求斜率
    if x2 == x1:
        return False
    return (y2 - y1)/(x2 - x1)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

if slope(x1, y1, x2, y2) == False and slope(x3, y3, x4, y4) == False:
    print("Yes")
elif slope(x1, y1, x2, y2) == slope(x3, y3, x4, y4):
    print("Yes")
else:
    print("No")