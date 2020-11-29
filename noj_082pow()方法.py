class Pow:
    def __init__(self, x, n):
        self.base = x
        self.power = n

    def cal(self):
        return self.base ** self.power

if __name__ == '__main__':
    x, n = map(int, input().split())
    pow = Pow(x, n)
    print(pow.cal())