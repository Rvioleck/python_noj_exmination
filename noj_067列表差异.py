list1 = input().split()
list1 = [int(i) for i in list1]
list2 = input().split()
list2 = [int(i) for i in list2]
result = []
for i in list1:
    if i in list1 and i not in list2:
        result.append(i)
for j in list2:
    if j in list2 and j not in list1:
        result.append(j)
for i in result:
    print(i, end=' ')