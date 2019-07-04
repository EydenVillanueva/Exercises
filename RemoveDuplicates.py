def remove_duplicates(nums):
    if nums:
        number = nums[0]
        i = 1

        while i < len(nums):                               
            if number == nums[i]:
                nums.pop(i)
                i -= 1
                print(i)                
            else:
                number = nums[i]
            i+=1
        
        return len(nums)    
    else:
        return 0


print(remove_duplicates([0,0,0,0,0,1,1,1,1,2,2,3,4,5,5,5,6,6,6,7,7,7,7,7,7,7,8]))