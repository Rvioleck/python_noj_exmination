set1 = set(input().split(' '))
set2 = set(input().split(' '))
set3 = set1 ^ set2
for i in sorted(set3):
    print(i, end=' ')