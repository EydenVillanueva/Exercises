def factorial(num):
    if num < 0:
        return num

    factorial = 1

    while num > 0:
        factorial *= num
        num-=1

    return factorial

def factorialr(num):
    if num < 0:
        return num
    
    return num * factorial(num-1)

if __name__ == "__main__":
    print(factorialr(4)) #24
    print(factorialr(6)) #720