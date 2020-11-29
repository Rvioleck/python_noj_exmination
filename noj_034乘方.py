def max_factor(num1):
    # 求num1的最大因数
    for i in range(num1//2+1, 0, -1):
        if num1%i == 0:
            return i

def unit_place(num1):
    # 求num1的个位数
    num1_str = str(num1)
    return int(num1_str[-1])

def power(num, exp):
    # 求num的exp次方的个位数
    num = unit_place(num)
    factor = max_factor(exp)
    exp /= factor
    num **= factor
    num = unit_place(num)
    result = int(str(num**exp)[-1])
    print(result)

power(123456789,123456789)