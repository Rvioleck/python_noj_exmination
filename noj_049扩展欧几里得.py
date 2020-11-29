a, b = map(int, input().split())
# 得出最大公约数
def MaxDivisor(d):
    a = d[0]
    b = d[1]
    while a%b != 0:
        tmp=a%b
        a = b
        b = tmp
    return b
acb = MaxDivisor([a, b])
#求值
def fun(a, b, acb):
    x = 1
    y = 0
    while True:
        y = (acb-x*a)//b
        if acb == a*x+b*y:
            return x, y
        x += 1
x, y = fun(a, b, acb)
print(x, y, sep = " ")


# def gcd(a, b):
#     if a <= b:
#         a,b = b,a
#     while b:
#         k = a%b
#         a = b
#         b = k
#     return a
#
# def ojld(a, b):
#     times = max(a, b) // min(a, b)
#     for i in range(-times, times+1):
#         for j in range(-times, times+1):
#             if a*i + b*j == gcd(a, b):
#                 print(i, j)
#                 return
#
# if __name__ == '__main__':
#     a, b = map(int, input().split())
#     ojld(a, b)