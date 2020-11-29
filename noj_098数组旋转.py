def list_left_movement(list1):
    first = list1[0]
    list1[0: -1] = list1[1: len(list1)]
    list1[-1] = first

list1 = list(map(int, input().split()))
n = int(input())
while n:
    list_left_movement(list1)
    n -= 1
for i in list1:
    print(i, end=' ')