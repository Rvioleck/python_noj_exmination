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
    if divisor == 1:
        return False
    else:
        return True

n, a, b = map(int, input().split())
value = a/b
gap_min = 1001
result_deno = 1
result_nume = 0
for denominator in range(1, n+1):
    numerator = int(denominator * value)
    gap = abs(numerator/denominator - value)
    if gap < gap_min and gap != 0 and ~most_common_divisor(denominator, numerator):
        gap_min = gap
        result_deno = denominator
        result_nume = numerator
print(result_nume, '/', result_deno, sep='')
