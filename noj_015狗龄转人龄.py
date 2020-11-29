def dog2human(dog_age):
    age_list = [10.5, 4]
    human_age = 0
    for i in range(dog_age):
        if i<=1:
            human_age += age_list[0]
        else:
            human_age += age_list[1]
    print(int(human_age))

age = int(input())
dog2human(age)
