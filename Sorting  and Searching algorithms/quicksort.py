def partition(array, low, high):
    i = (low-1) #index of the smaller element
    pivot = array[high] #pivot

    for j in range(low,high):
        #if current element is smaller that or equal to pivot
        if array[j] <= pivot:
            #increment index of smaller element
            i = i+1
            array[i],array[j] = array[j],array[i]
    
    array[i+1],array[high] = array[high],array[i+1]

    return (i+1)

def quickSort(array, low, high):
    if low < high:

        partition_index = partition(array,low,high)

        quickSort(array, low,partition_index-1)
        quickSort(array, partition_index+1, high)

if __name__ == "__main__":
    array = [3,10,7,4,8,9,1,6,2,5]
    n = len(array)
    quickSort(array,0,n-1)
    print("Sorted Array is: ")
    for i in range(n):
        print("%d" %array[i])