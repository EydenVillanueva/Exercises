def one_away(s1,s2):

    if s1 == s2:
        return True
    
    cont = 0

    if (len(s1) - 1 ) == len(s2):
        for i in range( len(s2) ):
            if not(s2[i] in s1):
                cont += 1
    
    else:
        for i in range (len(s2) ):
            if s1[i] != s2[i]:
                cont += 1
    
    if cont < 2:
        return True
    
    return False

print(one_away('pale','ple'))
print(one_away('pales','pale'))
print(one_away('pale','bale'))
print(one_away('pale','bake'))
