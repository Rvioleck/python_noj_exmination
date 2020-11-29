def factorial(num):
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        return result

def catalan(num):
    return int(factorial(2*num)/(factorial(num+1)*factorial(num)))

num = int(input())
print(catalan(num))