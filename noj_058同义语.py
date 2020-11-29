def synonym(str):
    if 'poor' not in str or 'not' not in str:
        return str
    else:
        pre_str = str[0: int(str.index('not'))]
        post_str = str[int(str.index('poor')) + 4: len(str)]
    return pre_str + 'good' + post_str


str = input()
while str != '':
    print(synonym(str))
    str = input()