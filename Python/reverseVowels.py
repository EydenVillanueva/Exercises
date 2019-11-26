def es_vocal(letra):
    letra = letra.lower()
    if letra == 'a' or letra == 'e' or letra == 'o' or letra == 'i' or letra == 'u':
        return True
    return False

def replace(s1,index,s2):
    s1 = list(s1)
    s1[index] = s2
    return "".join(s1)

def reverseVowels(s):
    
    cont = 0
    dic = {}
    
    for i in range(len(s)-1,0,-1):
        if es_vocal(s[i]):
            dic[cont] = s[i]
            cont+=1
    
    cont = 0
    
    for i in range(len(s)):
        if es_vocal(s[i]):
            s = replace(s,i,dic[cont])
            cont+=1
    
    return s

print(reverseVowels("leetcode")) #leotcede