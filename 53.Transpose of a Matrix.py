def transpose(matrix):
    for i in range(len(matrix)):
        for j in range (i+1,len(matrix)):
            matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]

    return matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]

print('Original Matrix->')

for i in matrix:print(i)

print(f'Transpose matrix->')

for i in transpose(matrix):print(i)