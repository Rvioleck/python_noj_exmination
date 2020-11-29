def dynamic_pro(m, n):
    # 青蛙过河动态规划
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i + 1
    for i in range(m + 1):
        for j in range(1, n + 1):
            dp[i][j] = 2 * dp[i][j-1]
    print(dp[m][n])

m, n = map(int, input().split(','))
while n >= 0 and m >= 0:
    # 任意m,n＜0时退出程序
    dynamic_pro(m, n)
    m, n = map(int, input().split(','))
