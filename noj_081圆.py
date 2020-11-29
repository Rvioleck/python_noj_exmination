class Circle:
    # circle的静态属性pi=3.14
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # calculate the area of the circle
        return self.pi * self.radius ** 2

    def perimeter(self):
        # calculate the perimeter of the circle
        return 2 * self.pi * self.radius

if __name__ == '__main__':
    radius = float(input())
    circle = Circle(radius)
    print("{:.2f} {:.2f}".format(circle.area(), circle.perimeter()))
