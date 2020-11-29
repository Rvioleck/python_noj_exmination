def eat_candy(n):
    # 列表plan[n]表示n个糖果的方案个数
    plan = [0 for _ in range(21)]
    plan[1] = 1
    plan[2] = 2
    for i in range(3, n+1):
        plan[i] = plan[i-1] + plan[i-2]
    return plan[n]

n = int(input())
while n != 0:
    print(eat_candy(n))
    n = int(input())