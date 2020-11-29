def collatz_conjecture(n):
    list = [n]
    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        list.append(int(n))
    return list

n = int(input())
list = collatz_conjecture(n)
for i in list:
    if i != list[-1]:
        print(i,',',sep='',end='')
    else:
        print(i,end='')