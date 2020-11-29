sentence = input()
words = sentence.split(' ')
lenofword = [len(word) for word in words]
print(words[lenofword.index(min(lenofword))], words[lenofword.index(max(lenofword))], sep='\n')