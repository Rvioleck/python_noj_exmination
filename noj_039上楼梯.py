def climb_stairs(num):
    # num 为楼梯阶数，上楼梯可1,2,3阶
    #最高100阶台阶
    method = [0 for _ in range(101)]
    method[1], method[2], method[3] = 1, 2, 4
    for i in range(4, num + 1):
        method[i] = method[i-1] + method[i-2] + method[i-3]
    return method[num]

num = int(input())
while num != 0:
    print(climb_stairs(num))
    num = int(input())

