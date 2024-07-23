def relative_sort(arr1,arr2):
    relative_array=[]
    #to sort the elements of arr1 in the order of arr2
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr2[i]==arr1[j]:
                relative_array.append(arr1[j])
    #remaining elements in arr1
    remaining_elements=[i for i in arr1 if i not in relative_array]
    remaining_elements.sort()

    return relative_array+remaining_elements

arr1=list(map(int,input('Enter the elements of arr1:').split(' ')))

arr2=list(map(int,input('Enter the elements of arr2:').split(' ')))

print(f'Relative sorted array is->{relative_sort(arr1,arr2)}')
