def isRightTriangle(a, b):
    if a < b:
        a, b = b, a
    c = (a**2 + b**2)**0.5
    if a + b > c and a + c > b and b + c > a and c.is_integer():
        return 'c'
    c = (a**2 - b**2)**0.5
    if a + b > c and a + c > b and b + c > a and c.is_integer():
        if c > b:
            return 'b'
        else:
            return 'a'
    return 'non'

a = int(input())
b = int(input())
print(isRightTriangle(a, b))