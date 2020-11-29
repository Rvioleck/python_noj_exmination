class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        # calculate the area of the rectangle
        return self.length * self.width

if __name__ == '__main__':
    l, w = map(int, input().split())
    rect = Rectangle(l, w)
    print(rect.area())