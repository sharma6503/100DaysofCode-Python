def rearrange_array(arr):
    even_idx,odd_idx=0,1
    rearranged_array=[0]*len(arr)
    for i in arr:
        if i>0:
            rearranged_array[even_idx]=i
            even_idx+=2
        else:
            rearranged_array[odd_idx]=i
            odd_idx+=2

    return rearranged_array


arr=list(map(int,input('Enter the array elements:').split(' ')))

print(f'Original Array->{arr}\n'
      f'Rearranged Array->{rearrange_array(arr)}')

