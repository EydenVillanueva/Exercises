
def replace(s1,index,s2):
    s1 = list(s1)
    s1[index] = s2
    return "".join(s1)

def urlify(s1):

    if s1 == "":
        return s1
    
    s1 = s1.strip()
    s1 = " ".join(s1.split())

    for i in range(len(s1)-1):
        if s1[i] == " ":
            s1 = replace(s1,i,"%20")

    return s1





print(urlify("Mr     John    Smith   "))
