def shift_list(list):
    temp = list[0]
    for i in range(1, len(list)):
        list[i-1] = list[i]
    list[len(list) - 1] = temp


def circle_list(list1, list2):
    for i in range(len(list1)):
        shift_list(list1)
        if list1 == list2:
            return True
    return False

list1 = input().split()
list2 = input().split()
print(circle_list(list1, list2))
