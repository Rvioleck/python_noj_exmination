n, k = map(int, input().split())
f = [0, 1]
i = 2
while n:
    f_i = f[i-1] + f[i-2]  # 添加入斐波那契数列
    f.append(f_i)
    if f[i] % k == 0:
        # 每发现一个k的倍数进行n的自减
        n -= 1
    i += 1
print(len(f)-1)