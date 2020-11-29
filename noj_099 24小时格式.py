timeAPM = input().split(" ")
if timeAPM[1] == "AM":
    lis = timeAPM[0].split(":")
    if int(lis[0]) == 12:
        lis[0] = "00"
    print(":".join(lis))
elif timeAPM[1] == "PM":
    lis = timeAPM[0].split(":")
    if int(lis[0]) != 12:
        lis[0] = str((int(lis[0]) + 12)%24)
    print(":".join(lis))



# clock, when = input().split()
# if when == 'PM':
#     if int(clock[0:2]) < 12:
#         clock = str(int(clock[0:2]) + 12)%24 + clock[2: len(clock)]
# elif when == 'AM':
#     if int(clock[0:2]) >= 12:
#         clock = str(int(clock[0:2]) - 12)%24 + clock[2: len(clock)] # [i for i in str(int(clock[0:2]) - 12)]
#
# print(clock)