def extract_string(list_str):
    # 提取字符串的前两个字母和后两个字母，若字符串长度小于2则返回原字符串
    for str0 in list_str:
        if len(str0) < 2:
            result = str0[:]
        else:
            result = str0[0:2] + str0[-2:len(str0)]
        print(result)


list_str = []
str1 = input()
while str1 != '':
    list_str.append(str1)
    str1 = input()
extract_string(list_str)
