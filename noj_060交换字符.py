pre_str = input()
s = ''.maketrans(',.','.,')
post_str = pre_str.translate(s)
print(post_str)