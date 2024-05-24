def is_equal(arr1,arr2):
    return ''.join(arr1)==''.join(arr2)

arr1=list(map(str,input('Enter first array elements:').split(' ')))

arr2=list(map(str,input('Enter second array elements:').split(' ')))

if is_equal(arr1,arr2):
    print(f'{arr1,arr2} are equal string arrays')
else:
    print(f'{arr1, arr2} are not equal string arrays')