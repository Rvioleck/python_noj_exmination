import math

def cylinder(height, radius):
    # calculate the volumn and area of the cylinder
    volumn = math.pi * radius * radius * height
    area = 2 * math.pi * radius * (radius + height)
    print("{:.4f}\n{:.4f}".format(volumn, area))

height = float(input())
radius = float(input())
cylinder(height, radius)