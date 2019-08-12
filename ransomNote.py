def ransomNote(s1,s2):

    if (not s1 and not s2) or (not s1 and s2):
        return True
    if not s2 and s1:
        return False

    dics1 , dics2 = {}, {}

    for s in s1:
        if s in dics1:
            dics1[s] += 1
        else:
            dics1[s] = 1

    for s in s2:
        if s in dics2:
            dics2[s] += 1
        else:
            dics2[s] = 1
    
    for k,v in dics1.items():
        if k in dics2:
            if not v <= dics2[k]:
                return False
        else:
            return False
    
    return True

if __name__ == "__main__":
    print(ransomNote("a","b"))#false
    print(ransomNote("aa","aab"))#true
    print(ransomNote("aa","ab"))#false