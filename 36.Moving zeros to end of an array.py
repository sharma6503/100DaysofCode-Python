
def move_zeros_to_end(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1



    return arr


arr_elements=list(map(int,input('Enter the array elements:').split(' ')))

print(f'Array Elements after Moving Zeros to end:'
      f'{move_zeros_to_end(arr_elements)}')
