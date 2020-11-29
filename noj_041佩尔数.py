def pell_number(n):
    pell = [0, 1]
    for i in range(2, n+1):
        num = 2 * pell[i-1] + pell[i-2]
        pell.append(num)
    return pell[n]

n = int(input())
print(pell_number(n))