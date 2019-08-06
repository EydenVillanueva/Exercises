def pivotIndex(array):
    sumas = []
    suma = 0
    
    for i,item in enumerate(array):
        if i == 0:
            sumas.append(item)
            suma+=item
        elif i > 0:
            suma += item
            sumas.append(suma)
    
    indexs = []

    for i in range(1,len(array)):
        if i != 0 and i != len(array):
            if sumas[i-1] == ( sumas[len(sumas)-1] - sumas[i]):
                indexs.append(i)

    if len(indexs) == 0:
        return -1
    else:
        return indexs[0]

if __name__ == "__main__":
    print(pivotIndex([2,3,5,4,1]))