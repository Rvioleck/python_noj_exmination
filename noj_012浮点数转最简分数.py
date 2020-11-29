"""
将浮点数转为最简分数
"""
# from fractions import Fraction
# print(Fraction(4.2))

def most_common_divisor(num1, num2):
    # 求num1和num2的最大公因子
    if num2 > num1:
        num1, num2 = num2, num1
    divisor = 1 # 返回值最大公因子
    i = 1 # 循环出口标志
    while i <= num2:
        if num1%i==0 and num2%i==0:
            if i >= divisor:
                divisor = i
        i += 1
    return divisor

def digitsnum_after_point(num=''):
    # 返回数num小数点后的位数，用于将分数化为分母为10的幂次的形式
    point_index = num.index('.')
    return len(num)-point_index

def fractor_print(num_str):
    # 打印浮点数(字符串所输入的)的最简分数形式
    factor = digitsnum_after_point(num_str)
    donominator = 10**factor
    numerator = float(num_str)*donominator
    m_c_divisor = most_common_divisor(donominator, numerator)
    donominator /= m_c_divisor
    numerator /= m_c_divisor
    print('{}/{}'.format(int(numerator), int(donominator)))

#main
fractor_print(num_str = input())