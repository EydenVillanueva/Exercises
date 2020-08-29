def rotateString(s1,s2):
    #Another Aproach
    #return len(s1) == len(s2) and s2 in s1+s1
    if (not A and B) or (not B and A):
        return False
    elif not A and not B:
        return True
    
    aux = s1

    while aux != s2:

        lista = list(aux)
        c = lista.pop(0)
        lista.append(c)
        aux = "".join(lista)

        if aux == s1:
            return False
    
    return True



if __name__ == "__main__":
    
    print(rotateString('abcde','cdeab'))
    print(rotateString('abcde','abced'))