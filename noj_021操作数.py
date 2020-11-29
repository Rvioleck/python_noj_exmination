"""
任意一个整数，每次减去它的各位之和，求操作的次数
"""
def subtract(num):
    # 每次减去各位之和
    digits = [int(i) for i in str(num)]
    num -= sum(digits)
    return num

def operand(num):
    # 求操作次数
    count = 0
    while num > 0:
        num = subtract(num)
        count += 1
    print(count)

num = int(input())
operand(num)