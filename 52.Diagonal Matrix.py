def check_diagonal(matrix):
    is_diagonal=True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i!=j and matrix[i][j]!=0:
                is_diagonal=False
    return True if is_diagonal else False

matrix=[[1,0,0],[0,1,0],[0,0,1]]

for i in matrix:print(i)

if check_diagonal(matrix):
    print(f'The given matrix is Diagonal Matrix')
else:
    print(f'The given matrix is not a diagonal matrix')