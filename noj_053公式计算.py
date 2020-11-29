def formula_calcu(str1, x, y, z):
    num = str(x) + str(y) + str(z)
    t = ''.maketrans('xyz', num)
    print(str1, '=', eval(str1.translate(t)), sep='')

str1 = input()
x, y, z = map(int, input().split())
formula_calcu(str1, x, y, z)
