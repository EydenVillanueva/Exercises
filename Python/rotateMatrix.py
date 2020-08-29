def rotateMatrix(matrix):
    size = len(matrix[0]) - 1
    lup = matrix[0]
    ldown = matrix[size]



print(rotateMatrix([
    [1,2,3],
    [8,9,4],
    [7,6,5]
]))