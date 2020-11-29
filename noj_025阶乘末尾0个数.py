import math
n = int(input())
n_fac = str(math.factorial(n))
count = 0
for i in range(len(n_fac)-1,0, -1):
    if n_fac[i] == '0':
        count += 1
    else:
        break
print(count)
