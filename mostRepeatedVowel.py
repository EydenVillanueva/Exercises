def replace(s1,index,s2):
    s1 = list(s1)
    s1[index] = s2
    return "".join(s1)

def es_vocal(letra):
    letra = letra.lower()
    if letra == 'a' or letra == 'e' or letra == 'o' or letra == 'i' or letra == 'u':
        return True
    return False

def repeatVowel(s):
    dic = {}
    vowel = ""
    maxi = 0

    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1
    
    for k,v in dic.items():
        if v > maxi:
            vowel = k
            maxi = v

    for indice,i in enumerate(s):
        if es_vocal(i):
            s = replace(s,indice,vowel)
    
    return s

if __name__ == "__main__":
    print(repeatVowel("hola gerardo"))