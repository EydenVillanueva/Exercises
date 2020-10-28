def flippingImage(matrix):
    if not matrix:
        return matrix

    for i, row in enumerate(matrix):
        row.reverse()
        for j in range(len(row)):
            if row[j] == 1:
                row[j] = 0
            else:
                row[j] = 1
        matrix[i] = row

    return matrix


if __name__ == "__main__":
    print(flippingImage([
        [1,1,1,0,0],
        [1,1,0,1,0],
        [1,1,0,1,0],
    ]))