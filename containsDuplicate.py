def containsDuplicate(nums, k):

    if len(nums) < k :
        return False

    j , i = len(nums) - 1, 0
    direccion = False
    vueltas = (len(nums)-1) * 2

    for v in range(vueltas):
        if nums[i] == nums[j]:
            if j - k == i:
                return True
        if direccion:
            i+= 1
        elif j - 1 == i:
            j = len(nums) - 1
            direccion = True
        else:
            j-= 1
    
    return False


if __name__ == "__main__":
    print(containsDuplicate([1,0,1,1],1)) # True
    print(containsDuplicate([1,2,3,1],3)) #True
    print(containsDuplicate([1,2,3,1,2,3],2)) #False