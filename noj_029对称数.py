def symmetry_number(num):
    #求数字num是否是中心对称
    #central_sym记录每个数字对应的对称数字，无则为-1
    central_sym = ['0', '1', '2', '-1', '-1', '5', '9', '-1', '8', '6']
    num_str = str(num)
    len_num = len(num_str)
    for i in range(len_num):
        # num_str[] = '916' num_str[0]=='9'==central_sym[6]==central_sym[int(num_str[len_num - i - 1])]
        if num_str[i] != central_sym[int(num_str[len_num - i - 1])]:
            return 'No'
    return 'Yes'

num = int(input())
print(symmetry_number(num))