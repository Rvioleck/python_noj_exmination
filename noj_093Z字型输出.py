def zigzag(list1, n):
    if n == 1:
        print(list1[0][0])
        return
    result = []
    for i in range(n):
        # 添加首行
        result.append(list1[0][i])
    for j in range(1, n-1):
        # 添加对角线
        result.append(list1[j][n-j-1])
    for i in range(n):
        # 添加末行
        result.append(list1[-1][i])
    for i in result:
        print(i, end=' ')

n = int(input())
list1 = []
for i in range(n):
    num = list(map(int, input().split()))
    list1.append(num)

zigzag(list1, n)