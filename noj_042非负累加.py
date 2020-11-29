def vector_sum(num, sum_):
    memo = [[0 for _ in range(sum_+1)] for __ in range(num+1)]
    for i in range(num+1):
        memo[i][0]= 1
        for n in range(1, num+1):
            for s in range(1, sum_+1):
                memo[n][s]= sum(memo[n-1][s-i] for i in range(s+1))
    return memo[num][sum_]

n,v = map(int, input().split())
print(vector_sum(n,v))