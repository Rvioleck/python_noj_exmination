def sort_dict(dict1):
    key_sort = sorted(dict1.items(), key = lambda dict1:dict1[0], reverse = True)
    value_sort = sorted(dict1.items(), key = lambda dict1:dict1[1], reverse = False)
    print(value_sort)
    print(key_sort)

if __name__ == '__main__':
    dict1 = {}
    string = input()
    while string != '':
        course, grade = string.split()
        dict1[course] = grade
        string = input()
    sort_dict(dict1)