def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        left = array[:mid]
        rigth = array[mid:]

        mergeSort(left)
        mergeSort(rigth)

        i,j,k = 0,0,0

        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = rigth[j]
                j+=1
            k+=1

        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1

        while j < len(rigth):
            array[k] = rigth[j]
            j+=1
            k+=1


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    print(arr)
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    print(arr)