def bubbleSort(array):
    if array:
        flag = False
        for i in range(len(array)):
            flag = False
            for j in range(len(array)-1):
                if array[j] > array[j+1]:
                    aux = array[j]
                    array[j] = array[j+1]
                    array[j+1] = aux
                    flag = True
            if not flag:
                break

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7] 
    print(arr) 
    bubbleSort(arr)
    print(arr)
    