#medium in-place
def findAllDup(nums):
    if not nums:
        return []
    
    dic = {}

    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1

    nums = []
    for k,v in dic.items():
        if v == 2:
            nums.append(k)
    
    return nums


if __name__ == "__main__":
    print(findAllDup([4,3,2,2,7,3]))