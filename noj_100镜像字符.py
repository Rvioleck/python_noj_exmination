import string

data = [i for i in input()]
n = int(input())
for i in range(n-1, len(data)):
    data[i] = chr(219 - ord(data[i]))

print("".join(data))