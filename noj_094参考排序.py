def reference_sort(data, index):
    zip1 = zip(data, index)
    dict1 = dict(zip1)
    dict_value_sort = sorted(dict1.items(), key = lambda d:d[1], reverse=False)
    result = [i[0] for i in dict_value_sort]
    return ' '.join(result)

data = input().split()
index = list(map(int, input().split()))
print(reference_sort(data, index))