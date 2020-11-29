def participle_adverb(word):
    if len(word) >= 3:
        if word[-3:len(word)] == 'ing':
            word += 'ly'
        else:
            word += 'ing'
    return word

word = input()
while word != '':
    print(participle_adverb(word))
    word = input()