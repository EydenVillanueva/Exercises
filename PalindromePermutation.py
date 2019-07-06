def fill_dict(s1):
    dic = {}
    for i in range(len(s1)):
        if s1[i] in dic:
            dic[s1[i]] += 1
        else:
            dic[s1[i]] = 1
    return dic

def palindrome_permutation(s1):
    s1 = s1.lower()
    s1 = s1.replace(" ","")

    if len(s1) < 2:
        return false
    if len(s1)%2 == 0:
        pair = True 
    else:
        pair = False

    dic = fill_dict(s1)

    if pair:
        for value in dic.values():
            if not(value%2 == 0):
                return False
        return True
    else:
        flag = False
        for value in dic.values():

            if not(value%2 == 0) and flag:
                return False

            elif not(value%2 == 0) and not(flag):
                flag = True
        return True

print(palindrome_permutation("anita lava la tina")) #True  'Taco cat'