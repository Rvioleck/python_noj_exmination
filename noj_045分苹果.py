def apple_divided(apple, plate):
    if apple == 0 or plate == 1:
        return 1
    if plate > apple:
        return apple_divided(apple, apple)
    else:
        return apple_divided(apple, plate - 1) + apple_divided(apple-plate, plate)

apple, plate = map(int, input().split())
print(apple_divided(apple, plate))