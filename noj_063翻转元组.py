string = input()
pre_tuple = tuple(string.split(' '))
post_tuple = pre_tuple[::-1]
result = tuple([int(pre_tuple[i]) + int(post_tuple[i]) for i in range(len(pre_tuple))])
print(result)