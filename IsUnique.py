def unique(word):
    dic = {}
    for letter in word:
        if letter in dic:
            return False
        else:
            dic[letter] = 1
    return True

#inplace algorithm
def uniquee(word):
    for i,letter in enumerate(word,1):
        if letter in word[i:len(word)]:
            return False
    return True


print(uniquee("eyden me llamo carolina"))
print(uniquee("abcdefghijkmnopqrs tu"))
print(uniquee("hla mundo"))