files = input()
files_name = files.split(',')
files_num = []
for file_name in files_name:
    file_num = file_name[1: len(file_name)]
    files_num.append(int(file_num))
files_num.sort(reverse=False)
for file in files_num:
    print('a', file, sep='', end=' ')