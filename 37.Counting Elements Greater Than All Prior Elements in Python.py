def count_greater_element(arr):
    prev=-1
    count=0
    for i in arr:
        if i>prev:
            prev=i
            count+=1
    return count

arr_elements=list(map(int,input('Enter array elements:').split(' ')))

print(f'Number of elements greater than'
      f' its prior elements are {count_greater_element(arr_elements)}')