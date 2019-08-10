def binarySearch(array,target): 
    left = 0
    rigth = len(array) - 1
  
    while left <= rigth: 
        mid = int(left + (rigth - left)/2); 
          
        if array[mid] == target: 
            return mid 
  
        elif array[mid] < target: 
            left = mid + 1
  
        else: 
            rigth = mid - 1
      
    return -1

if __name__ == "__main__":
    print(binarySearch([1,2,3,4],2)) #1