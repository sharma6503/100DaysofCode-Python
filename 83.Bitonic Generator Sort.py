def bitonic_generator_sort(arr):
    even_idx_elements,odd_idx_elements=[],[]
    for i in range(len(arr)):
        if i%2==0:
            even_idx_elements.append(arr[i])
        else:
            odd_idx_elements.append(arr[i])
    even_idx_elements.sort()
    odd_idx_elements.sort(reverse=True)
    arr[:]=even_idx_elements+odd_idx_elements
    return arr

arr=list(map(int,input('Enter array elements:').split(' ')))

print(f'Original Array->{arr}\n'
      f'Bitonic sorted Array->{bitonic_generator_sort(arr)}')
