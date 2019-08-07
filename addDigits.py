def addDigits(number):

    if len(str(number)) == 1:
        return number
    
    suma = 0
    for i in str(number):
        suma+= int(i)
    
    return addDigits(suma)


if __name__ == "__main__":
    print(addDigits(99))