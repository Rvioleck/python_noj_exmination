list = input().split(',')
key = []
value = []
for i in list:
    key1, value1 = i.split(':')
    key.append(key1)
    value.append(int(value1))
print(max(value), min(value))