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

def print_result(result_den, result_num, operator):
    divisor = most_common_divisor(result_den, result_num)
    result_den /= divisor
    result_num /= divisor
    print("({}/{}){}({}/{})={}/{}".format(num1, den1, operator, num2, den2, int(result_num), int(result_den)))

def fractor_add(num1, den1, num2, den2):
    #分数相加
    result_den = den1*den2
    result_num = num1*den2 + num2*den1
    print_result(result_den, result_num, '+')

def fractor_sub(num1, den1, num2, den2):
    # 分数相减
    result_den = den1*den2
    result_num = num1*den2 - num2*den1
    print_result(result_den, result_num, '-')

def fractor_multiply(num1, den1, num2, den2):
    # 分数相乘
    result_den = den1*den2
    result_num = num1*num2
    print_result(result_den, result_num, '*')

def fractor_divide(num1, den1, num2, den2):
    # 分数相除
    result_den = den1*num2
    result_num = num1*den2
    print_result(result_den, result_num, '/')

num1 = int(input())
den1 = int(input())
num2 = int(input())
den2 = int(input())
fractor_add(num1, den1, num2, den2)
fractor_sub(num1, den1, num2, den2)
fractor_multiply(num1, den1, num2, den2)
fractor_divide(num1, den1, num2, den2)