def numberOfSegments(s):
    cSegmentos = 0

    for i,c in enumerate(s):
        if i > 0:
            if c == ' ' and s[i-1] != ' ':
                cSegmentos+=1
        if c != ' ' and i == len(s) - 1:
            cSegmentos+=1
    
    return cSegmentos

if __name__ == "__main__":
    print(numberOfSegments("he")) #5