def isValidBoomerang(puntos):

    punto1 = puntos[0]
    punto2 = puntos[1]
    punto3 = puntos[2]

    if punto2[1] > punto1[1] and punto2[1] > punto3[1]:
        return True
    elif punto2[1] < punto1[1] and punto2[1] < punto3[1]:
        return True
    if punto2[0] > punto1[0] and punto2[0] > punto3[0]:
        return True
    elif punto2[0] < punto1[0] and punto2[0] < punto3[0]:
        return True

    return False

if __name__ == "__main__":
    print(isValidBoomerang([[1,1], [2,2], [3,3]]))