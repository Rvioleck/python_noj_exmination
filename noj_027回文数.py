def is_parlindrome(num_str):
    reversed_str = num_str[::-1]
    if reversed_str == num_str:
        return 'Yes'
    return 'Not'

num = input()
print(is_parlindrome(num))