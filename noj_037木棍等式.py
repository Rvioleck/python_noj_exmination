def stick_number(num):
    # 函数返回两位数字num需要的火柴个数
    # 记录下数字0~9需要的火柴个数
    stick_num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    result = 0
    if num < 10:
        result = stick_num[num]
    elif 10 <= num < 100:
        # 返回个位和十位的火柴个数
        result = stick_num[num%10] + stick_num[num//10]
    elif 100 <= num < 1000:
        result = stick_num[num%10] + stick_num[(num//10)%10] + stick_num[num//100]
    else:
        result = stick_num[num%10] + stick_num[(num//10)%10] + stick_num[num//100%10] + stick_num[num//1000]
    return result

def stick_eqution(n):
    count = 0
    if n <= 4:
        print(count)
    else:
        n -= 4 # 减去+和=用去的4根火柴
        for num1 in range(1000):
            for num2 in range(1000):
                if stick_number(num1) + stick_number(num2) + stick_number(num1 + num2) == n:
                    count += 1
    print(count)

n = int(input())
stick_eqution(n)