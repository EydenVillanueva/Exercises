
def check_permutation(s1,s2):

    if s1 == s2:
        return False
    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()

    for letter in s1:
        if not(letter in s2):
            return False
    
    for letter in s2:
        if not(letter in s1):
            return False
    
    return True


print(check_permutation("abcd","dcba")) #True
print(check_permutation("eyden","eeydn")) #True
print(check_permutation("eydenas","eeydn")) #False
print(check_permutation("eyden","iyden")) #False
print(check_permutation("eyden","eydea")) #False