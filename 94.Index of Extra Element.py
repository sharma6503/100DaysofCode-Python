def find_index(arr1,arr2):
    extra_element=set(arr1).difference(set(arr2))
    idx_of_extra_element=extra_element.pop()

    return arr1.index(idx_of_extra_element)


arr1=list(map(int,input('Enter elements of arr1:').split(' ')))

arr2=list(map(int,input('Enter elements of arr2:').split(' ')))

print(f'The Extra Element Present in the index of->{find_index(arr1,arr2)} ')