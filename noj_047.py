# coding:utf-8
def decomposition(num, factor):
    if num == 1:
        return 1
    if factor == 1:
        return 0
    if num % factor == 0:
        return decomposition(num/factor, factor) + decomposition(num, factor - 1)
    else:
        return decomposition(num, factor - 1)

num = int(input())
print(decomposition(num, num))