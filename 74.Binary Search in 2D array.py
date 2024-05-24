def binary_search(matrix,target):
    start=0
    m=len(matrix)
    n=len(matrix[0])
    end=m*n-1
    while start<=end:
        mid=(start+end)//2
        row=mid//n
        col=mid%n
        if matrix[row][col]==target:
            return [row,col]
        elif matrix[row][col]<target:
            start=mid+1
        else:
            end=mid-1
    return False

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=11

if binary_search(matrix,target)!=False:
    print(f'The target is found')
else:
    print(f'The target is not found')
