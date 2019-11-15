# Single Number Exercise
# Follow-up: in-place algorithm

def singleNumber(array):
    dic = {}

    for item in array:
        if not(item in dic):
            dic[item] = 1
        else:
            dic[item] += 1
    
    for k,v in dic.items():
        if v == 1:
            return k

def singleNumberInPlace(array):
    for item in enumerate(array):
        if array.count(item) == 1:
            return item
    return 0
        

if __name__ == "__main__":
    print(singleNumber([2,2,1])) # 1
    print(singleNumber([4,1,2,1,2])) # 4
    print(singleNumber([1,2,3,4,5,5])) # 1
    print(singleNumber([2,2,4,4,5,2,5,3])) # 3

    print(singleNumberInPlace([2,2,1])) # 1
    print(singleNumberInPlace([2,2,1])) # 1
    print(singleNumberInPlace([4,1,2,1,2])) # 4
    print(singleNumberInPlace([1,2,3,4,5,5])) # 1