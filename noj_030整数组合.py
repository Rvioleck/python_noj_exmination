def integer_conbination(n, m):
    # 输出n+nn+nnn+nnnn+....共m组的和
    n_nums = []
    n_num = 0
    for i in range(m):
        n_num += n
        n *= 10
        n_nums.append(n_num)
    return sum(n_nums)

n = int(input())
m = int(input())
print(integer_conbination(n, m))