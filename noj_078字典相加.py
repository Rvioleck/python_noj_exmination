def dict_sum(dict1, dict2):
    dict3 = {}
    for key, value in dict1.items():
        if key not in dict2.values():
            dict3[key] = int(value)
    for key, value in dict2.items():
        if key not in dict1.values():
            dict3[key] = int(value)
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if key1 == key2:
                dict3[key1] = int(value1) + int(value2)
    print(dict3)

list1 = input().split(',')
list2 = input().split(',')
key1, key2 = [], []
value1, value2 = [], []
for i in list1:
    key, value = i.split(':')
    key1.append(key)
    value1.append(value)
dict1 = dict(zip(key1, value1))
for i in list2:
    key, value = i.split(':')
    key2.append(key)
    value2.append(value)
dict2 = dict(zip(key2, value2))
dict_sum(dict1, dict2)

