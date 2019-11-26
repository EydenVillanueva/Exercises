def max_consecutive(nums):
    if len(nums) < 0:
        return 0
    
    maximo = 0
    actual = 0
    
    for i in range(len(nums)):
        print(nums[i])
        if nums[i] == 1:
            actual+=1
        else:
            if actual > maximo:
                maximo = actual
            actual = 0
    
    if actual > maximo:
        return actual
    return maximo

print(max_consecutive([1,0,1,1,0,1]))