def queue_up(m, n):
    if n == 0:
        # 石柱为0个，荷叶为m个的时候，可供m+1个青蛙过河
        print(m + 1)
    else:
        # 每一个石柱够两倍的m+1个青蛙过河
        print(2**n * (m + 1))

m, n = map(int, input().split(','))
while n >= 0 and m >= 0:
    # 任意m或n＜0时退出程序
    queue_up(m, n)
    m, n = map(int, input().split(','))
