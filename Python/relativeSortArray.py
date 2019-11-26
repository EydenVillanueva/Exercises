def relativeSortArray(a1,a2):
    if len(a1) < len(a2):
        return []

    cont, aux= 0,0

    for i in range(len(a2)):
        for j in range(len(a1)):
            if a2[i] == a1[j]:
                aux = a1[cont]
                a1[cont] = a1[j]
                a1[j] = aux
                cont += 1
    return a1


if __name__ == "__main__":
    print(relativeSortArray([2,4,1,5,4,2,3],[2,1,4,5,3]))