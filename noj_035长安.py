def chang_an(bx, by, px=10, py=10):
    # 全部初始化为0
    dp = [[0 for i in range(11)] for j in range(11)]
    # 边界初始化为1
    for i in range(bx + 1):
        dp[i][0] = 1
    for j in range(by + 1):
        dp[0][j] = 1
    # 动态规划 dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for i in range(1, bx + 1):
        for j in range(1, by + 1):
            if i == px and j == py:
                # 遇到点p，此路不通，置0
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[bx][by])

bx, by, px, py = map(int, input().split(','))
while bx >= 0 and by >= 0 and px >= 0 and py >= 0:
    chang_an(bx, by, px, py)
    bx, by, px, py = map(int, input().split(','))
