def division_algo(quotient):
    remainder = 1
    for divisor in range(10, 100): # 除数divisor为两位数
        dividend = divisor * quotient + remainder
        if 1000 <= dividend <= 9999: # 被除数dividend为四位数
            print(dividend, divisor)

division_algo(709)