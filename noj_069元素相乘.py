list = input().split()
list = [int(i) for i in list]
result = 1
for i in list:
    result *= i
print(result)