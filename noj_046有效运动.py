def effective_movement(x1, y1, x2, y2):
    if x2 < x1 or y2 < y1:
        return 'false'
    dp = [[0 for i in range(y2 + 1)] for i in range(x2 + 1)]
    dp[x1][y1] = 1
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if i + j > x2 and j + i <= y2:
                dp[i][j+i] = dp[i][j]
            elif i + j <= x2 and j + i > y2:
                dp[i+j][j] = dp[i][j]
            elif i + j > x2 and j + i > y2:
                break
            else:
                dp[i][j+i] = dp[i][j]
                dp[i+j][j] = dp[i][j]
    if dp[x2][y2] == 1:
        return 'true'
    else:
        return 'false'

x1, y1, x2, y2 = map(int, input().split())
print(effective_movement(x1, y1, x2, y2))
