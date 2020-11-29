def single_digit(num1):
    # 求num1的个位数
    num1_str = str(num1)
    return int(num1_str[-1])

def power1(num, exp):
    # 求num的exp次方的个位数
    _1 = [1]
    _2 = [2, 4, 8, 6]
    _3 = [3, 9, 7, 1]
    _4 = [4, 6]
    _5 = [5]
    _6 = [6]
    _7 = [7, 9, 3, 1]
    _8 = [8, 4, 2, 6]
    _9 = [9, 1]
    list = [_1, _2, _3, _4, _5, _6, _7, _8, _9]
    digit = single_digit(num)
    cycles_num = exp % len(list[digit-1])
    print(list[digit-1][cycles_num-1])

num, exp = map(int, input().split())
while num > 0 and exp > 0:
    power1(num, exp)
    num, exp = map(int, input().split())