def isChess(matrix):
    for i in range( len(matrix[0]) ):
        for j in range( len(matrix[0]) ):
            if ( i == 0 or i%2 == 0) and ( j == 0 or j%2 == 0):
                if matrix[i][j] != 1:
                    return False
            elif i%2 != 0 and j%2 != 0:
                if matrix[i][j] != 1:
                    return False
    return True


if __name__ == "__main__":
    matrix = [
        [1,0,1,0,1],
        [0,1,0,1,0],
        [1,0,1,0,1],
        [0,1,0,1,0],
        [1,0,1,0,1]
    ]
    print(isChess(matrix))