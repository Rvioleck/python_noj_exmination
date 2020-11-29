def takeSecond(list):
    return list[1]

string = input()
strings_list = string.split(';')
tuples_list = [eval(i) for i in strings_list]
tuples_list.sort(key=takeSecond)
print(tuples_list)

# temp_2 = tuples_list[0][len(tuples_list[0]) - 1]
# for i in range(1, len(tuples_list) - 1):
#     if tuples_list[i][len(tuples_list[i]) - 1] < temp_2:
