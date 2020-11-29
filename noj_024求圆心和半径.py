def get_distance(x1, y1, x2, y2):
    # calculate the distance between two points
    return ((y2 - y1)**2 + (x2 - x1)**2)**0.5

def cal_circle(x1, y1, x2, y2, x3, y3):
    # calculate the radius and center of the circle
    A = x1 * (y2 - y3) - y1*(x2-x3)+x2*y3-x3*y2
    B = (x1**2+y1**2)*(y3-y2)+(x2**2+y2**2)*(y1-y3)+(x3**2+y3**2)*(y2-y1)
    C = (x1**2+y1**2)*(x2-x3)+(x2**2+y2**2)*(x3-x1)+(x3**2+y3**2)*(x1-x2)
    D = (x1**2+y1**2)*(x3*y2-x2*y3)+(x2**2+y2**2)*(x1*y3-x3*y1)+(x3**2+y3**2)*(x2*y1-x1*y2)
    x = -B/(2*A)
    y = -C/(2*A)
    r = ((B**2+C**2-4*A*D)/(4*A**2))**0.5
    print("{:.3f},{:.3f},{:.3f}".format(r, x, y))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
cal_circle(x1, y1, x2, y2, x3, y3)