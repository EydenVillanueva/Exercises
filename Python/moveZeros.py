def moveZeros(nums):
    cont = 0
    contzeros = 0
    size = len(nums) - 1

    for i in range(size):
        if nums[i] == 0:
            nums.append(0)
            contzeros +=1
            
    if contzeros:
        for i in range(size):                
            if nums[cont] == 0:
                del nums[cont]
            else:
                cont += 1
    return nums