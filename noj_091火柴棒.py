def match_stick(n):
    if n <= 0:
        return False
    # f(n) = 3n + f(n-1)
    num = 3 * (n + 2) * ( n - 1 ) / 2 + 3
    return int(num)

n = int(input())
print(match_stick(n))