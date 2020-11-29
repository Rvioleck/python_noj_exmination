string = input()
strs = string.split(' ')
nums = [int(str) for str in strs]
nums.sort(reverse=True)
for num in nums:
    print(num, end=' ')