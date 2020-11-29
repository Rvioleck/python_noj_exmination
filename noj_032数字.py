def number(n):
    for a1 in range(n, 0, -1):
        for a2 in range(n, 0, -1):
            if (a1+a2)%2 != 0:
                continue
            for a3 in range(n, 0, -1):
                if  (a2+a3)%3 == 0 and (a1+a2+a3)%5 == 0:
                    max = a1+a2+a3
                    return max

n = int(input())
print(number(n))