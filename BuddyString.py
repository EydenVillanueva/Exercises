def buddy(A,B):
    if len(A) < 1 or len(B) < 1:
        return False
    if A == B:
        cont = len(A)-1
        for i in range(len(A)-1):
            if(A[i] != B[cont]):
                return False
            cont -= 1  
        return True
    if len(B) != len(A):
        return False

    buffer = []
    for i in range (len(B)):
        if A[i] != B[i]:
            buffer.append(A[i])
            buffer.append(B[i])

    if len(buffer) == 4:
        print(buffer)
        if buffer[1] == buffer[2] and buffer[0] == buffer[len(buffer) - 1]:
            return True
    
    return False
        


print(buddy("abc","acc")) #False
print(buddy("abc","acb")) #True
print(buddy("aaaaaed","aaaaaed")) #False                                                                              #False
