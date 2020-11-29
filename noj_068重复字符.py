str = input()
result = {}
for i in str:
    result[i] = str.count(i)

for key,value in result.items():
    if value > 1:
        print(key,value)