def phonenumber(str):
    net_id = int(str[0:2])
    if str.isdigit():
        if len(str) == 11:
            if net_id in [13, 14, 15, 17, 18, 19]:
                return True
    return False

str = input()
while str != '':
    print(phonenumber(str))
    str = input()