def find_non_repeating_elements(arr):
    return [i for i in arr if arr.count(i)==1]

arr_elements=list(map(int,input('Enter the array elements:').split(' ')))

print(f'The Non Repeating elements in the array are :'
      f'{(find_non_repeating_elements(arr_elements))}')
