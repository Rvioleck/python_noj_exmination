num = int(input())
list = input().split()
tuple = tuple([int(i) for i in list])
print(tuple.count(num))