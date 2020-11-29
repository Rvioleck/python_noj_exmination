def reverse_binary(num):
    binary_num = bin(num)
    return binary_num[-1:1:-1]

num = int(input())
print(reverse_binary(num))