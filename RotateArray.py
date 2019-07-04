
def rotate(nums, k):
    if k <= 0:
        return 0
    
    aux = nums.copy()
    cont = 0
    
    if k > len(nums):
        pos = k % len(nums)
    else:
        pos = k

    for i in range(pos, len(nums)):
        nums[i] = aux[cont]
        cont+=1

    for i in range(0,pos):
        nums[i] = aux[cont]
        cont+=1

    print(nums)


rotate([1,2,3,4,5,6,7],10)