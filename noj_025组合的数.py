n = int(input())
count = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if 0 <= n-a-b-c <= 9:
                count += 1
print(count)