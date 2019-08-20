def detectCapital(string):
    if not string:
        return False
    if string.isupper() or string.islower():
        return True
    
    if string[0].isupper:
        for i,c in enumerate(string):
            if c.isupper() and i != 0:
                return False
        return True
    
    return False

if __name__ == "__main__":
    print(detectCapital("USA"))
    print(detectCapital("usa"))
    print(detectCapital("Usa"))
    print(detectCapital("uSa"))
    print(detectCapital("USa"))