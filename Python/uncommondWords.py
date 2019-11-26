def uncommond(a,b):
    if a == None or b == None:
        return []
    
    words = []
    dic = {}

    a_lista = a.split(" ")
    b_lista = b.split(" ")

    for word in a_lista:
        if not(word in dic):
            dic[word] = 1
    
    for word in b_lista:
        if word in dic:
            dic[word] += 1
        if not(word in dic):
            dic[word] = 1

    for word in dic:
        if dic[word] == 1:
            words.append(word)
    
    return words
    

print(uncommond("apple apple","bannana"))