n = int(input())
key = [i for i in range(1, n+1)]
value = [i*i for i in key]
zip1 = zip(key, value)
dict1 = dict(zip1)
print(dict1)