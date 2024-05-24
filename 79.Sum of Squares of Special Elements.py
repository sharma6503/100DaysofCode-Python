def sum_of_squares_of_special_elements(arr):
    special_elements=[]
    for i in range(len(arr)):
        if len(arr)%(i+1)==0:
            special_elements.append(arr[i]**2)
    return sum(special_elements)

arr=list(map(int,input('Enter the array elements:').split(' ')))

print(f'The sum of squares of special elements is->'
      f'{sum_of_squares_of_special_elements(arr)}')
