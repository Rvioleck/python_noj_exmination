def delete_odd(str1=''):
    str0 = str1[::2]
    print(str0)

str1 = input()
while str1 != '':
    delete_odd(str1)
    str1 = input()