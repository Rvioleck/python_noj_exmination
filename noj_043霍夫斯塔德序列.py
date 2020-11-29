def hofstadter_sequence(n):
    male = [0]
    female = [1]
    for i in range(1, n+1):
        num_male = i - female[male[i-1]]
        male.append(num_male)
        num_female = i - male[female[i-1]]
        female.append(num_female)
    print(female[n], male[n])

n = int(input())
hofstadter_sequence(n)